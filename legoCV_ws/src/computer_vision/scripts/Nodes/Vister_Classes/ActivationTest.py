#!/usr/bin/env python3
from cv2 import imwrite
import rospy
import sys, os
import cv2
import numpy as np
from sensor_msgs.msg import Image
from computer_vision.msg import ActivationTestInfo
from computer_vision.srv import Robo
from cv_bridge import CvBridge, CvBridgeError
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))

#sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
import BoundingBox 
import DataFile
import VideoSaver
import MalfunctionVideoSaver

class ActivationTest:
    
    def __init__(self):
        self.project_name = "Activation Test"                                                                        #NEEDS TO COME FROM USER
        self.file_name = None
        self.start_frame = None
        self.current_frame = None
        self.called = 1 
        self.img = None
        self.first_lap_run = False
        self.testVideo = 0
        self.path = None

        #self.testStarted = False
        self.nrOfLaps = None
        self.lapCounter = 0
        self.rois = []
        self.test_started = False
        self.camera_ready = False
        
        #Variables to Check for Malfunctions
        self.control_positions = []
        self.pos_buffer = 4.5  

        self.w_mean = None
        self.size_buffer = 4
        self.h_mean = None
         
        self.temp_data = []
        self.result = []
        
        #Variables for data output
        self.malfunctions = []

        #Create subscriber to camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)
        
        #Create subscriber to Setup Node
        self.setupSub = rospy.Subscriber("ActivationTest", ActivationTestInfo, self.setupCallback)


        self.rate = rospy.Rate(1)
        self.roboService = rospy.ServiceProxy("RunNextLap", Robo)

        

### SETUP #############################################################################################################
    def setupCallback(self, data):
        if self.current_frame is not None:
            self.unpack_message(data)
            self.setup_datafile()
            self.setup_testfile()
            self.setupSub.unregister()
            self.start_test()

    def unpack_message(self,data):
        self.file_name = data.FileName
        self.nrOfLaps = data.Lap
        self.testVideo = data.TestVideo
        self.path = data.DataPath
        cnt = 0
        for roi in data.Rois:
            self.malfunctions.append(0)
            temp_roi = []
            for element in range(len(roi.RoiInfo)):
                temp_roi.append(roi.RoiInfo[element])
            self.rois.append(temp_roi)
            cnt += 1

    def setup_datafile(self):
        header = [' ']
        for r in range(len(self.rois)):
            header.append('Object'+str(r+1))                                                                 
        self.malfunctionFile = DataFile.DataFile(self.file_name,self.path, header)
    
    def setup_testfile(self):
        newFileName = self.file_name + "_test"
        header = [' ']
        for r in range(len(self.rois)):
            header.append('Object'+str(r+1))
            header.append('X'+str(r+1))
            header.append('Y'+str(r+1))
            header.append('W'+str(r+1))
            header.append('H'+str(r+1))                                                                 
        self.testFile = DataFile.DataFile(newFileName,self.path, header)

### STARTING ##########################################################################################################
    def start_test(self):
        self.start_frame = self.current_frame
        self.BB = BoundingBox.BoundingBox(len(self.rois))  
        if self.testVideo == True:
            print("Was true, so making a video")
            self.testVS = VideoSaver.VideoSaver(self.file_name, self.path)
        self.get_control_data()
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
        self.process_control_position(bb_data)
        self.process_control_size(bb_data)


    def process_control_position(self, control_data):
        for bb in range(len(control_data)):
            self.control_positions.append([control_data[bb][0], control_data[bb][1]])
        
    def process_control_size(self, control_data):
        w_list = []
        h_list = []
        for bb in range(len(control_data)):
            w_list.append(control_data[bb][2])
            h_list.append(control_data[bb][3])
        self.w_mean = np.mean(w_list)
        self.h_mean = np.mean(h_list)
    
    def before_first_lap(self):
        print("\n[MSG] Setup is completed.")
        print("\n[MSG] Test is running, don't shutdown computer.")  
        if self.testVideo == True:
            print("calling total video")
            self.testVS.start_recording()
        self.first_lap_run = True

    def run_robot(self, request):
        #Create service to Robot
        rospy.wait_for_service("RunNextLap")
        if self.first_lap_run == False:
            self.before_first_lap()
       
        self.roboService(request)
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
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
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
            self.testVS.change_text("Lap nr: "+str(self.lapCounter+1))
            sys.stdout.write("\r")
            sys.stdout.write("\n{:3d} laps done." .format(self.lapCounter))
            sys.stdout.flush()
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
            imName = "lap"+str(self.lapCounter)+"Roi"+str(cnt)+".jpg"
            if self.lapCounter %10 == 0:
                cv2.imwrite(os.path.join(self.path,imName), temp)
        self.temp_data = self.BB.get_data()
        self.BB.clear_data()
    
    def process_data(self):
        self.save_testdata()
        self.check_position()
        self.check_size()
        self.update_malfunctions()
        

    def check_position(self):
        for i in range(len(self.rois)):
            x,y = self.control_positions[i]
            x_new,y_new,_,_ = self.temp_data[i]
            if x_new in range(x-self.pos_buffer, x+self.pos_buffer):
                if y_new in range(y-self.pos_buffer, y+self.pos_buffer):
                    self.result.append(1)
                else:
                    self.result.append(0)
            else:
                self.result.append(0)
      
       
    def check_size(self):
        for i in range(len(self.rois)):
            _,_,w,h = self.temp_data[i]
            if (w not in range(int(self.w_mean-self.size_buffer), int(self.w_mean+self.size_buffer))):
                if (h not in range(int(self.h_mean-self.size_buffer), int(self.h_mean+self.size_buffer))):
                    self.result[i]= 0

    def update_malfunctions(self):
        malfunction_occured = False
        for i in range(len(self.rois)):
            if self.result[i] == 0 and self.malfunctions[i] == 0:
                self.malfunctions[i] = self.lapCounter
                malfunction_occured = True
    
    def save_testdata(self):
        row = ['']
        for i in range(len(self.rois)):
            row.append('')
            row.append(self.temp_data[i][0])
            row.append(self.temp_data[i][1])
            row.append(self.temp_data[i][2])
            row.append(self.temp_data[i][3]) 
        self.testFile.save_data(row)                                                                
    
        

### TEST DONE ##############################################################################################################
    def stop_test(self):
        if self.testVideo == True:
            self.testVS.stop_recording()
        self.save_data()
        print("The test has been completed and the data is saved.")
        self.camSub.unregister()
        cv2.destroyAllWindows()

    def save_data(self):
        row = ['Malfunction detected after lap:']
        for r in range(len(self.rois)):
            if self.malfunctions[r] != 0:
                row.append(self.malfunctions[r])
            else:
                row.append('')                                                                 
        self.malfunctionFile.save_data(row)