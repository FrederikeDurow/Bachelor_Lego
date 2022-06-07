#!/usr/bin/env python3
import os
import sys
import time

import cv2
import numpy as np
import rospy
from computer_vision.msg import MotionTrackerInfo
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
from collections import OrderedDict

import CentroidTracker
import DataFile
import Object_Color_Detector
import VideoSaver


class MotionTracker:

    project_name = "Motion Tracker Test" 

    def __init__(self):
        #Setup Variables                                                               
        self.file_name = None
        self.start_frame = None
        self.current_frame = None
        self.nr_of_laps = None
        self.lap_counter = 0
        self.total_roi = []
        self.lap_roi = []
        self.test_started = False
        self.H= None
        self.W= None
        self.detections = []
        self.crop_img = None
        self.objects = OrderedDict()
        self.path = None

        #Tracker Variables
        self.position = True
        self.old_position = True
        self.timer_started = False
        self.test_start_time = 0
        self.lap_start_time = 0
        self.lap_time = 0
        self.color = None

        #Create subscriber to Setup Node
        self.setup_sub = rospy.Subscriber("LiveMotionTracking", MotionTrackerInfo, self.setupCallback)

        #Create subscriber to camera
        self.cam_sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

        #create Centroid Tracker
        self.tracker = CentroidTracker.centroidTracker()
        self.detector = Object_Color_Detector.obj_color_dectector()

### SETUP #############################################################################################################
    def setupCallback(self, data):
        self.unpackMessage(data)
        self.setup_sub.unregister()
        print("\n[MSG] Setup is completed.")
        self.startTest()
        
    def unpackMessage(self, data):
        self.file_name = data.FileName
        self.nr_of_laps = data.Lap
        self.path = data.DataPath
        self.hsv_low = data.HSV_lower
        self.hsv_up = data.HSV_upper
        cnt = 0
        for roi in data.Rois:
            temp_roi = []
            for element in range(len(roi.RoiInfo)):
                temp_roi.append(roi.RoiInfo[element])
            if cnt == 0:
                self.total_roi = temp_roi
                cnt = 1
            elif cnt == 1: 
                self.lap_roi = [temp_roi[0]-self.total_roi[0],temp_roi[1]-self.total_roi[1], temp_roi[2], temp_roi[3]] 

    def startTest(self):
        self.VS = VideoSaver.VideoSaver(self.file_name, self.path)
        self.VS.startRecording()
        self.setupDatafile()
        self.updateTimer()
        self.test_started = True
        print("\n[MSG] Test is running, don't shutdown computer.")  

    def setupDatafile(self):
        header = ["Motion Tracking Test", "Lap", "Time pr Lap"]                                                                
        self.lapFile = DataFile.DataFile(self.file_name,self.path,header)                                                

### RUNNING ###########################################################################################################
    def camCallback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            print(e)
        if self.test_started == True and self.current_frame is not None:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                self.stopTest()
            self.prepImage()
            
            self.VS.changeText("Lap nr: "+str(self.lap_counter+1))
            self.detections = self.detector.applyColorDectector(self.crop_img, self.hsv_low, self.hsv_up, 200)
            self.objects = self.tracker.update(self.detections)
            self.drawID()
            cv2.rectangle(self.crop_img, (self.lap_roi[0],self.lap_roi[1]), (self.lap_roi[0]+self.lap_roi[2], self.lap_roi[1]+self.lap_roi[3]), (0,255,0), 2)
            cv2.imshow(self.project_name, self.crop_img)
            self.checkPosition()
            self.updateLaps()
            
            if self.lap_counter == self.nr_of_laps:
                self.stopTest()
        
    def prepImage(self):
        blurred = cv2.GaussianBlur(self.current_frame, (11, 11), 0)
        self.crop_img = blurred[self.total_roi[1] : self.total_roi[1]+self.total_roi[3], self.total_roi[0] : self.total_roi[0]+self.total_roi[2]]

    def drawDetections(self):
        if  self.detections is not None:
            for i in range(len(self.detections)):
                (startX, startY, endX, endY,_) = self.detections[i]
                cv2.rectangle(self.crop_img, (startX,startY), (startX+endX, startY+endY), (0,255,0), 2)

    def drawID(self):
        if self.objects is not None:
            for (objectID, centroid) in self.objects.items():
                text = "ID {}".format(objectID)
                cv2.putText(self.crop_img, text, (centroid[0]-10, centroid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
                cv2.circle(self.crop_img, (centroid[0], centroid[1]), 4, (0,0,255), -1)

  
    def checkPosition(self):
        self.old_position = self.position
        if self.objects is not None:
            for (_, centroid) in self.objects.items():                                                         
                if centroid[0] in range(self.lap_roi[0],self.lap_roi[0]+self.lap_roi[2]):
                    if centroid[1] in range(self.lap_roi[1],self.lap_roi[1]+self.lap_roi[3]):
                        self.position = True
                    else:
                        self.position = False
                else: 
                    self.position = False
        
    def updateLaps(self):
        if self.old_position == False and self.position == True:
            self.lap_counter += 1
            self.updateTimer()
            self.saveData()
            sys.stdout.write("\r")
            sys.stdout.write("\n{:3d} laps done." .format(self.lap_counter))
            sys.stdout.flush()
        

    def updateTimer(self):
        if self.timer_started == False:
            self.timer_started = True
            self.test_start_time = time.time()
            self.lap_start_time = time.time()
        self.lap_time = time.time() - self.lap_start_time
        self.lap_start_time = time.time()
       
### TEST DONE ##############################################################################################################
    def stopTest(self):
        self.VS.stopRecording()
        print("\n[MSG] The test has been completed and the data is saved.")
        self.cam_sub.unregister()
        cv2.destroyAllWindows()

    def saveData(self):
        row = ['', self.lap_counter, self.lap_time]                                                             
        self.lapFile.saveData(row)
        if self.lap_counter == self.nr_of_laps:
            row = ['', "Total Time: ", time.time()-self.test_start_time]                                                             
            self.lapFile.saveData(row)
