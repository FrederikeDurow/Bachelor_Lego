#!/usr/bin/env python3
import os
import sys

import cv2
import numpy as np
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
from computer_vision.msg import ActivationTestInfo, RoiList

import ROIs


class ActivationTestSetup:

    def __init__(self):
        #Initializations for Camera Stream
        self.current_frame = None
        self.window_name = 'Camera Live Stream'
        self.sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.callback)

        #Initializations for Test Info
        self.test_type = None
        self.nr_of_laps = 0
        self.file_name = None
        self.path = None
        self.rois = []
        self.test_video = 0
        
        #Initializations for Regions of Interest
        self.new_rois = ROIs.ROIs(self.window_name)

        #Initialization of message
        self.msg = None
        

    def callback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            print(e)
        self.current_frame = self.new_rois.drawRois(self.current_frame)
        cv2.imshow(self.window_name, self.current_frame)
        cv2.waitKey(10)

    def setTestInfo(self):
        self.setLaps()
        self.setVideoSettings()
        self.setPath()
        self.setFileName()
        self.setRois()
        self.publishInfo()

    def setLaps(self):
        print("\n[USER INPUT] Please enter number of laps:")
        self.nr_of_laps = input()

    def getLaps(self):
        return self.nr_of_laps
    
    def setRois(self):
        print("\n[USER INPUT] Choose all regions of interest.")
        self.new_rois.setMultiRois()
        self.rois = self.new_rois.getRois()
    
    def getRois(self):
        return self.new_rois.getRois()

    def setPath(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = input()
    
    def setFileName(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.file_name = input()
    
    def setVideoSettings(self):
        print("\n[USER INPUT] Do you want to save a video of the whole test? (y/n)")
        while True:
            k = input()
            if k == "y" or k == "n":
                self.test_video = k
                break
            else:
                pass

    def createTestMessage(self):
        info = ActivationTestInfo()
        info.FileName = self.file_name
        info.Lap = int(self.nr_of_laps)
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        if self.test_video == "y":
            info.TestVideo = True
        else:
            info.TestVideo = False
        info.DataPath = self.path
        self.msg = info
    
    def publishInfo(self):
        self.createTestMessage()
        testPub = rospy.Publisher("ActivationTest", ActivationTestInfo, queue_size=10)
        robotPub = rospy.Publisher("StartRobot", String, queue_size=10)
        rate = rospy.Rate(10) 
        self.sub.unregister()
        cv2.destroyWindow(self.window_name)
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            robotPub.publish(self.path)
            rate.sleep()
