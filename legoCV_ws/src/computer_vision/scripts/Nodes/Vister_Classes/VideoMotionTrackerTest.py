#!/usr/bin/env python3
import os
import sys

import cv2
import rospy
from computer_vision.msg import MotionTrackerInfo

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
from collections import OrderedDict

import CentroidTracker
import DataFile
import Object_Color_Detector


class MotionTracker:

    def __init__(self):
        #Setup Variables
        self.project_name = "Motion Tracker Test"                                                                        #NEEDS TO COME FROM USER
        self.file_name = None
        self.current_frame = None
        self.nr_of_laps = None
        self.lap_counter = 0
        self.total_roi = []
        self.lap_roi = []
        self.detections = []
        self.crop_img = None
        self.objects = OrderedDict()
        self.path = None
        self.videoPath = None

        #Tracker Variables
        self.position = True
        self.old_position = True
        self.lap_time = 0
      
        self.fps = 0
        self.frame_counter = 0
        self.last_lap_frame = 0

        #Create subscriber to Setup Node
        self.setup_sub = rospy.Subscriber("VideoMotionTracking", MotionTrackerInfo, self.setupCallback)

        #Create Color Detector and Centroid Tracker
        self.detector = Object_Color_Detector.obj_color_dectector()
        self.tracker = CentroidTracker.centroidTracker()

### SETUP #############################################################################################################
    def setupCallback(self, data):
        self.unpackMessage(data)
        self.setup_sub.unregister()
        print("\n[MSG] Setup is completed.")
        self.startTest()
        
    def unpackMessage(self, data):
        self.file_name = data.FileName
        self.nr_of_laps = data.Lap
        self.videoPath = data.VideoPath
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
        self.setupDataFile()
        self.updateTimer()
        print("\n[MSG] Test is running, don't shutdown computer.")  
        self.runTest()

    def setupDataFile(self):
        header = ["Motion Tracking Test", "Lap", "Time pr Lap"]                                                                
        self.lapFile = DataFile.DataFile(self.file_name,self.path,header)

                                                      

### RUNNING ###########################################################################################################
    def runTest(self):
        video = cv2.VideoCapture(self.videoPath)
        self.fps = video.get(cv2.CAP_PROP_FPS)
        ret, self.current_frame = video.read()
        cv2.imshow("video", self.current_frame)
        cv2.waitKey(1)
        while True:
            ret, self.current_frame = video.read()
            if ret: 
                self.prepImage()
                self.frame_counter = self.frame_counter+1
                
                self.detections = self.detector.applyColorDectector(self.crop_img, self.hsv_low, self.hsv_up, 200)
                self.objects = self.tracker.update(self.detections)
                self.drawID()
                cv2.rectangle(self.crop_img, (self.lap_roi[0],self.lap_roi[1]), (self.lap_roi[0]+self.lap_roi[2], self.lap_roi[1]+self.lap_roi[3]), (0,255,0), 2)
                cv2.imshow(self.project_name, self.crop_img)
                cv2.waitKey(1)
                self.checkPosition()
                self.updateLaps()
               
            else: 
                break
        video.release()
        cv2.destroyAllWindows()
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
            for (objectID, centroid) in self.objects.items():                                                           #FIX: WE NEED TO MAKE SURE WE ONLY HAVE ONE OBJECT
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
        print("last frame: " + str(self.last_lap_frame))
        print("Frame counter: " + str(self.frame_counter))
        print("FPS: " + str(self.fps))
        print("lap time: " + str(self.lap_time))
        if self.lap_counter == 1:
            self.lap_time = self.last_lap_frame/self.fps
        elif self.lap_counter > 1:
            self.lap_time = (self.frame_counter - self.last_lap_frame)/self.fps
        else:
            pass
        self.last_lap_frame  = self.frame_counter
       
### TEST DONE ##############################################################################################################
    def stopTest(self):
        print("\n[MSG] The test has been completed and the data is saved.")

        cv2.destroyAllWindows()

    def saveData(self):
        row = ['', self.lap_counter, self.lap_time]                                                             
        self.lapFile.saveData(row)
        if self.lap_counter == self.nr_of_laps:
            row = ['', "Total Time: ", (self.last_lap_frame)/self.fps]                                                             
            self.lapFile.saveData(row)
