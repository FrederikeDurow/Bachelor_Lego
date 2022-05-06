#!/usr/bin/env python3
from cv2 import imwrite
import rospy
import sys
import cv2
import numpy as np
from sensor_msgs.msg import Image
from computer_vision.msg import ProjectInfo
from computer_vision.srv import Robo
from cv_bridge import CvBridge, CvBridgeError

sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import BoundingBox 
from Classes import DataFile
from Classes import VideoSaver

class ActivationTest:
    
    def __init__(self):
        self.project_name = "Activation Test"                                                                        #NEEDS TO COME FROM USER
        self.file_name = None
        self.start_frame = None
        self.current_frame = None
        self.called = 0 
        self.img = None
        self.video_started = False

        #self.testStarted = False
        self.nrOfLaps = None
        self.lapCounter = 0
        self.rois = []
        self.test_started = False
        self.camera_ready = False
        
        #Variables to Check for Malfunctions
        self.control_positions = []
        self.w_min = None
        self.h_min = None
        self.w_max = None
        self.h_max = None
        self.x_buffer = 5                                                                                           #GÆT - SKAL RETTES
        self.y_buffer = 5
        self.temp_data = []
        self.result = []
        
        #Variables for data output
        self.malfunctions = []

        #Create subscriber to camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)
        
        #Create subscriber to Setup Node
        self.setupSub = rospy.Subscriber("ActivationTest", ProjectInfo, self.setupCallback)

        

### SETUP #############################################################################################################
    def setupCallback(self, data):
        if self.current_frame is not None:
            self.file_name = data.FileName
            self.nrOfLaps = data.Lap
            cnt = 0
            # for i in range(len(data.Rois)):
            #     self.malfunctions.append(0)
            for roi in data.Rois:
                self.malfunctions.append(0)
                temp_roi = []
                for element in range(len(roi.RoiInfo)):
                    temp_roi.append(roi.RoiInfo[element])
                self.rois.append(temp_roi)
                cnt += 1
            print(self.rois)
            self.setup_datafile()
            self.setupSub.unregister()
            self.start_test()
    
    def setup_datafile(self):
        header = [' ']
        for r in range(len(self.rois)):
            header.append('Object'+str(r))                                                                 
        self.malfunctionFile = DataFile.DataFile(self.file_name,header)

### STARTING ##########################################################################################################
    def start_test(self):
        self.start_frame = self.current_frame
        self.BB = BoundingBox.BoundingBox(len(self.rois))  
        self.VS = VideoSaver.VideoSaver(self.file_name)
        self.get_control_data()
        #self.process_control_data(bb_data)
        self.test_started = True                                          
        self.run_robot(True)

    def get_control_data(self):
        cnt = 0
        for roi in self.rois:
            cnt += 1
            crop_img = self.current_frame[roi[1]:roi[1]+roi[3],roi[0]:roi[0]+roi[2]]
            self.BB.applyBoundingBox(crop_img)
            temp = self.BB.drawBoundingbox()
            cv2.imwrite("ControlRoi"+str(cnt)+".jpg", temp)
        bb_data=self.BB.get_data()
        self.BB.clear_data()
        self.process_control_data(bb_data)

    def process_control_data(self, control_data):
        w_list = []
        h_list = []
        for bb in range(len(control_data)):
            self.control_positions.append([control_data[bb][0], control_data[bb][1]])
            w_list.append(control_data[bb][2])
            h_list.append(control_data[bb][3])
        self.w_min = np.mean(w_list) - np.var(w_list)*5
        self.w_max = np.mean(w_list) + np.var(w_list)*5
        self.h_min = np.mean(h_list) - np.var(h_list)*5
        self.h_max = np.mean(h_list) + np.var(h_list)*5
    
    def run_robot(self, request):
        #Create service to Robot
        rospy.wait_for_service("RunNextLap")
        if self.video_started == False:
            self.VS.start_recording()
            self.video_started == True
        self.rate = rospy.Rate(1)
        roboService = rospy.ServiceProxy("RunNextLap", Robo)
        roboService(request)
        if request == True:
            self.roboCallback()
            self.rate.sleep()
        else:
            pass

### RUNNING ###########################################################################################################
    def camCallback(self,data):
        self.camera_ready = True
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        except CvBridgeError as e:
            print(e)
        if self.test_started == True:
            if self.current_frame is not None:
                cv2.imshow(self.project_name, self.current_frame)
                cv2.waitKey(10)

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]]) 
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)


    def roboCallback(self):
        if self.called == 0:
            self.called = 1
            self.lapCounter += 1
            print("Laps run:" + str(self.lapCounter))
            self.get_data()
            self.process_data()
            if self.lapCounter == self.nrOfLaps:                                                
                self.run_robot(False)
                self.stop_test()
            else:
                self.run_robot(True)
        elif self.called == 1:
            self.called = 0
            self.run_robot(True)
    
    def get_data(self):
        cnt = 0
        self.temp_data = []
        for roi in self.rois:
            cnt += 1
            crop_img = self.current_frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]
            self.BB.applyBoundingBox(crop_img)
            temp = self.BB.drawBoundingbox()
            cv2.imwrite("lap"+str(self.lapCounter)+"Roi"+str(cnt)+".jpg", temp)
        self.temp_data = self.BB.get_data()
        self.BB.clear_data()
        #self.BB.save_data(self.lapCounter)
    
    def process_data(self):
        #self.BB.get_data()
        self.check_position()
        self.check_size()
        self.update_malfunctions()
        

    def check_position(self):
        # print("Control Positions:")
        # print(self.control_positions)
        for i in range(len(self.rois)):
            x,y = self.control_positions[i]
            x_new,y_new,_,_ = self.temp_data[i]
            # print("Roi nr " + str(i)+ " x: " +str(x_new) +", y: "+ str(y_new))
            if x_new in range(x-self.x_buffer, x+self.x_buffer):
                if y_new in range(y-self.y_buffer, y+self.y_buffer):
                    self.result.append(1)
                else:
                    self.result.append(0)
            else:
                self.result.append(0)
        #print(self.result)
       
    def check_size(self):
        # print("Control w_min: " + str(self.w_min) + ", w_max: " + str(self.w_max))
        # print("Control h_min: " + str(self.h_min) + ", h_max: " + str(self.h_max))
        for i in range(len(self.rois)):
            _,_,w,h = self.temp_data[i]
            # print("Roi nr " + str(i)+ " w: " +str(w) +", h: "+ str(h))
            if (w not in range(int(self.w_min), int(self.w_max))) or (h not in range(int(self.h_min), int(self.h_max))):
                self.result[i]= 0

    def update_malfunctions(self):
        for i in range(len(self.rois)):
            if self.result[i] == 0 and self.malfunctions[i] == 0:
                self.malfunctions[i] = self.lapCounter

### TEST DONE ##############################################################################################################
    def stop_test(self):
        self.VS.stop_recording()
        self.save_data()
        print("The test has been completed and the data is saved.")
        #Stop all subscriptions, publisher and windows
        self.camSub.unregister()
        #self.roboSub.unregister()
        cv2.destroyAllWindows()

    def save_data(self):
        row = ['Malfunction detected after lap:']
        for r in range(len(self.rois)):
            if self.malfunctions[r] != 0:
                row.append(self.malfunctions[r])
            else:
                row.append('')                                                                 
        self.malfunctionFile.save_data(row)