#!/usr/bin/env python3
import os
import sys

import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
from computer_vision.msg import MotionTrackerInfo, RoiList

import ROIs


class MotionTrackerSetup:

    def __init__(self):
        #Initializations for Camera Stream
        self.current_frame = None
        self.window_name = "Motion Tracker Test"
        self.sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.callback)
        
        #Initializations for Test Info
        self.nr_of_laps = 0
        self.file_name = None
        self.rois = []
        self.path = None
        self.hsv_low = []
        self.hsv_up = []
        
        #Initializations for Regions of Interest
        self.new_rois = ROIs.ROIs(self.window_name)

        #Initialization of message
        self.msg = None
        self.trackbar = "Not Running"

        #Flags
        self.create_trackbars = 0
            
    def callback(self, data):
        cv2.namedWindow(self.window_name,cv2.WINDOW_NORMAL)
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            print(e)
        self.current_frame = self.new_rois.drawRois(self.current_frame)
        
        if self.trackbar == "Not Running":
            cv2.imshow(self.window_name, self.current_frame)
            cv2.waitKey(1)
            
        elif self.trackbar == "Running":
            self.setHSV()

    def setHSV(self):
        if self.create_trackbars == 1:
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
            phMin = psMin = pvMin = phMax = psMax = pvMax = 0
            print("\n[USER INPUT] Press 's' to save chosen threshold")
            self.create_trackbars = 0
    
        else:
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
            hsv = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
            result = cv2.bitwise_and(self.current_frame, self.current_frame, mask=mask)

            # Display result image
            self.current_frame = self.new_rois.drawRois(self.current_frame)
            cv2.imshow(self.window_name, result)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                self.trackbar = "Not running"
                self.hsv_low= [hMin, sMin, vMin]
                self.hsv_up = [hMax, sMax, vMax]
                cv2.destroyAllWindows()
                self.publishInfo()
            else:
                pass

    def setTestInfo(self):
        self.setLaps()
        self.setRois()
        self.setPath()
        self.setFileName()
        self.trackbar = "Running"
        self.create_trackbars = 1
        
    def setLaps(self):
        print("\n[USER INPUT] Please enter number of laps:")
        self.nr_of_laps = input()

    def getLaps(self):
        return self.nr_of_laps
    
    def setRois(self):
        print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        self.new_rois.setSingleRoi()
        print("\n[USER INPUT] Choose where a lap starts/ends.")
        self.new_rois.setSingleRoi()
        self.rois = self.new_rois.getRois()
    
    def getRois(self):
        return self.new_rois.getRois()

    def setPath(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = str(input())
       
    def setFileName(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.file_name = input()

    def createTestMessage(self):
        info = MotionTrackerInfo()
        info.FileName = self.file_name
        info.Lap = int(self.nr_of_laps)
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
        testPub = rospy.Publisher("LiveMotionTracking", MotionTrackerInfo, queue_size=10)
        rate = rospy.Rate(10) #10Hz
        self.sub.unregister()
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()

def nothing(x):
    pass
