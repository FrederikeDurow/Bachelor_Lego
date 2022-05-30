#!/usr/bin/env python3
import math
import os
import sys

import cv2
import rospy
from computer_vision.msg import ActivationTestInfo
from computer_vision.srv import Robo
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
import BoundingBox
import DataFile
import VideoSaver

class ActivationTest:
    project_name = "Activation Test" 

    def __init__(self):

        #Variables for Setup                                                                   
        self.file_name = None
        self.current_frame = None
        self.called = 1 
        self.first_lap_run = False
        self.test_video = 0
        self.path = None
        self.nr_of_laps = None
        self.lap_counter = 0
        self.rois = []
        self.test_started = False
        
        #Variables to Check for Malfunctions
        self.pos_buffer = []
        self.x_buffer =  10
        self.y_buffer = 10

        self.w_mean = None
        self.h_mean = None
        self.w_min = None
        self.w_max = None
        self.h_min = None
        self.h_max = None
        self.size_buf = 6.5
        self.size_buffer = []
        
         
        self.temp_data = []
        self.result = []
        
        self.malfunctions = []

        #Create subscriber to camera
        self.cam_sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)
        
        #Create subscriber to Setup Node
        self.setup_sub = rospy.Subscriber("ActivationTest", ActivationTestInfo, self.setupCallback)


        self.rate = rospy.Rate(1)
        self.robo_service = rospy.ServiceProxy("RunNextLap", Robo)

### SETUP #############################################################################################################
    def setupCallback(self, data):
        if self.current_frame is not None:
            self.unpackMessage(data)
            self.setupDatafile()
            self.setup_sub.unregister()
            self.startTest()

    def unpackMessage(self,data):
        self.file_name = data.FileName
        self.nr_of_laps = data.Lap
        self.test_video = data.TestVideo
        self.path = data.DataPath
        cnt = 0
        for roi in data.Rois:
            self.malfunctions.append(0)
            temp_roi = []
            for element in range(len(roi.RoiInfo)):
                temp_roi.append(roi.RoiInfo[element])
            self.rois.append(temp_roi)
            cnt += 1

    def setupDatafile(self):
        header = [' ']
        for r in range(len(self.rois)):
            header.append('Object'+str(r+1))                                                                 
        self.malfunctionFile = DataFile.DataFile(self.file_name,self.path, header)

### STARTING ##########################################################################################################
    def startTest(self):
        self.BB = BoundingBox.BoundingBox()  
        if self.test_video == True:
            self.testVS = VideoSaver.VideoSaver(self.file_name, self.path)
        self.getControlData()
        self.test_started = True                                        
        self.runRobot(True)

    def getControlData(self):
        cnt = 0
        for roi in self.rois:
            cnt += 1
            crop_img = self.current_frame[roi[1]:roi[1]+roi[3],roi[0]:roi[0]+roi[2]]
            self.BB.applyBoundingBox(crop_img)
        bb_data=self.BB.getData()
        print("Control Data:")
        print(bb_data)
        self.BB.clearData()
        self.processControlPosition(bb_data)
        self.processControlSize(bb_data)


    def processControlPosition(self, control_data):
        for bb in range(len(control_data)):
            x,y,_,_ = control_data[bb]
            x_min = math.floor(x-(x/100*self.x_buffer))
            x_max = math.ceil(x+(x/100*self.x_buffer))
            y_min = math.floor(y-(y/100*self.y_buffer))
            y_max = math.ceil(y+(y/100*self.y_buffer))
            self.pos_buffer.append([x_min,x_max,y_min,y_max])
        print('Position buffer:')
        print(self.pos_buffer)

    def processControlSize(self, control_data):
        for bb in range(len(control_data)):
            _,_,w,h = control_data[bb]
            w_min = math.floor(w - (w/100*self.size_buf))
            w_max = math.ceil(w + (w/100*self.size_buf))
            h_min = math.floor(h - (h/100*self.size_buf))
            h_max = math.ceil(h + (h/100*self.size_buf))
            self.size_buffer.append([w_min,w_max,h_min,h_max])
        print('Width interval: (' + str(w_min) + "," + str(w_max) + ')')
        print('Height interval: (' + str(h_min) + "," + str(h_max) + ')')

    def beforeFirstLap(self):
        print("\n[MSG] Setup is completed.")
        print("\n[MSG] Test is running, don't shutdown computer.")  
        if self.test_video == True:
            self.testVS.startRecording()
        self.first_lap_run = True

    def runRobot(self, request):
        #Create service to Robot
        while True:
            rospy.wait_for_service("RunNextLap")
            if self.first_lap_run == False:
                self.beforeFirstLap()
        
            self.robo_service(request)
            if request == True:
                #self.roboCallback()
                if self.called == 0:
                    self.called = 1
                    self.lap_counter += 1
                    if self.test_video == True:
                        self.testVS.changeText("Lap nr: "+str(self.lap_counter+1))
                    sys.stdout.write("\r")
                    sys.stdout.write("\n{:3d} laps done." .format(self.lap_counter))
                    sys.stdout.flush()
                    self.getData()
                    self.processData()
                    if self.lap_counter == self.nr_of_laps:                                                
                        request = False
                        break
                    else:
                        request = True
                elif self.called == 1:
                    self.called = 0
                    request = True
                self.rate.sleep()
            else:
                pass
        self.stopTest()
    
    def roboCallback(self):
        if self.called == 0:
            self.called = 1
            self.lap_counter += 1
            if self.test_video == True:
                self.testVS.changeText("Lap nr: "+str(self.lap_counter+1))
            sys.stdout.write("\r")
            sys.stdout.write("\n{:3d} laps done." .format(self.lap_counter))
            sys.stdout.flush()
            self.getData()
            self.processData()
            if self.lap_counter == self.nr_of_laps:                                                
                self.runRobot(False)
                self.stopTest()
            else:
                self.runRobot(True)
        elif self.called == 1:
            self.called = 0
            self.runRobot(True)

### RUNNING ###########################################################################################################
    def camCallback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            print(e)
        if self.test_started == True:
            if self.current_frame is not None:
                cv2.imshow(self.project_name, self.current_frame)
                cv2.waitKey(10)

    def getData(self):
        cnt = 0
        self.temp_data = []
        for roi in self.rois:
            cnt += 1
            crop_img = self.current_frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]
            self.BB.applyBoundingBox(crop_img)
            temp = self.BB.drawBoundingbox()
            imName = "lap"+str(self.lap_counter)+"Roi"+str(cnt)+".jpg"
            if self.lap_counter %100 == 0:
                cv2.imwrite(os.path.join(self.path,imName), temp)
        self.temp_data = self.BB.getData()
        self.BB.clearData()
    
    def processData(self):
        self.checkPosition()
        self.checkSize()
        self.updateMalfunctions()
        
    def checkPosition(self):
        self.result = []
        for i in range(len(self.rois)):
            x_new,y_new,_,_ = self.temp_data[i]
            x_min,x_max,y_min,y_max = self.pos_buffer[i]
            
            if x_new in range(int(x_min), int(x_max)):
                if y_new in range(int(y_min), int(y_max)):
                    self.result.append(1)
                else:
                    self.result.append(0)
            else:
                self.result.append(0)
        print("after check_pos, length is: " + str(len(self.result)))
        print(self.result)
    
    
    def checkSize(self):
        for i in range(len(self.rois)):
            _,_,w,h = self.temp_data[i]
            w_min,w_max,h_min,h_max = self.size_buffer[i]
            if (w not in range(int(w_min), int(w_max))) or (h not in range(int(h_min), int(h_max))):
                self.result[i]= 0
            else:
                pass
        print("after check_size, length is: " + str(len(self.result)))
        print(self.result)

    def updateMalfunctions(self):
        for i in range(len(self.rois)):
            if self.result[i] == 0 and self.malfunctions[i] == 0:
                self.malfunctions[i] = self.lap_counter
                
### TEST DONE ##############################################################################################################
    def stopTest(self):
        if self.test_video == True:
            self.testVS.stopRecording()
        self.saveData()
        print("\nThe test has been completed and the data is saved.")
        self.cam_sub.unregister()
        cv2.destroyAllWindows()

    def saveData(self):
        row = ['Malfunction detected after lap:']
        for r in range(len(self.rois)):
            if self.malfunctions[r] != 0:
                row.append(self.malfunctions[r])
            else:
                row.append('')                                                                 
        self.malfunctionFile.saveData(row)
