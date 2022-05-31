#!/usr/bin/env python3
import os
import sys

import cv2
import numpy as np
import rospy

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
from computer_vision.msg import MotionTrackerInfo, RoiList

import ROIs


class MotionTrackerSetup:

    def __init__(self):
        self.initial_frame = None
        self.window_name = "Motion Tracker Test"
        
        #Initializations for Test Info
        self.video_path = None
        self.file_name = None
        self.path = None
        self.hsv_low = []
        self.hsv_up = []

        #Initialization of message
        self.msg = None
        self.trackbar = "Not Running"

        #Variables for ROI
        self.temp_roi = []
        self.rois = []
        self.roi_state = 0

    def setTestInfo(self):
        self.getVideo()
        self.setRois()
        self.setPath()
        self.setFileName()
        self.trackbar = "Running"
        self.setHSV()
        

    def getVideo(self):
        print("\n[USER INPUT] Please enter the path to the video:")
        self.video_path = input()

    def setRois(self):
        cap = cv2.VideoCapture(self.video_path)
        _, self.initial_frame = cap.read()
        
        print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        roi = cv2.selectROI(self.initial_frame)
        self.rois.append(roi)
        print("\n[USER INPUT] Choose where a lap starts/ends.")
        roi = cv2.selectROI(self.initial_frame)
        self.rois.append(roi)
    
    def addRoi(self, event,x,y,flags,*params):
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.setUpperLeft(x,y)   
        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            self.setLowerRight(x,y)
        else: 
            pass

    def setUpperLeft(self, x, y):
        self.temp_roi = []
        self.temp_roi.append(x)
        self.temp_roi.append(y)
        self.roi_state = 1
        pass

    def setLowerRight(self, x, y):
        self.temp_roi.append(x-self.temp_roi[0])
        self.temp_roi.append(y-self.temp_roi[1])
        self.rois.append(self.temp_roi)
        self.roi_state = 0
        pass

    def setPath(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = str(input())
       
    def setFileName(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.file_name = input()

    def createTestMessage(self):
        info = MotionTrackerInfo()
        info.VideoPath = self.video_path
        info.FileName = self.file_name
        info.DataPath = self.path
        info.HSV_lower = self.hsv_low
        info.HSV_upper = self.hsv_up
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        self.msg = info

    def publishInfo(self):
        self.createTestMessage()
        testPub = rospy.Publisher("VideoMotionTracking", MotionTrackerInfo, queue_size=10)
        rate = rospy.Rate(10) #10Hz
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()
    
    def setHSV(self):
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(self.window_name, self.initial_frame)
        cv2.waitKey(1)
        
        # Create trackbars to set HSV values
        cv2.createTrackbar('Hue_Min', self.window_name, 0, 179, nothing)
        cv2.createTrackbar('Sat_Min', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Val_Min', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Hue_Max', self.window_name, 0, 179, nothing)
        cv2.createTrackbar('Sat_Max', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Val_Max', self.window_name, 0, 255, nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('Hue_Max', self.window_name, 179)
        cv2.setTrackbarPos('Sat_Max', self.window_name, 255)
        cv2.setTrackbarPos('Val_Max', self.window_name, 255)

        # Initialize HSV min/max values
        hMin = sMin = vMin = hMax = sMax = vMax = 0
        print("\n[USER INPUT] Press 's' to save chosen threshold")
    
        while True:
            hMin = cv2.getTrackbarPos('Hue_Min', self.window_name)
            sMin = cv2.getTrackbarPos('Sat_Min', self.window_name)
            vMin = cv2.getTrackbarPos('Val_Min', self.window_name)
            hMax = cv2.getTrackbarPos('Hue_Max', self.window_name)
            sMax = cv2.getTrackbarPos('Sat_Max', self.window_name)
            vMax = cv2.getTrackbarPos('Val_Max', self.window_name)

            # Set minimum and maximum HSV values to display
            self.HSV_lower = np.array([hMin, sMin, vMin])
            self.HSV_upper = np.array([hMax, sMax, vMax])

            # Convert to HSV format and color threshold
            hsv = cv2.cvtColor(self.initial_frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
            result = cv2.bitwise_and(self.initial_frame, self.initial_frame, mask=mask)

            cv2.imshow(self.window_name, result)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                self.trackbar = "Not running"
                self.hsv_low= [hMin, sMin, vMin]
                self.hsv_up = [hMax, sMax, vMax]
                cv2.destroyAllWindows()
                self.publishInfo()
                break
            else:
                pass

def nothing(x):
    pass
