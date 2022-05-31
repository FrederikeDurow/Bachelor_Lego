#!/usr/bin/env python3
import os

import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


class MalfunctionVideoSaver:
    test_status = "Waiting"
    image_counter = 0
    cv_img = None

    def __init__(self, path):
        self.path = path
        self.video_name = None
        
        #Create subscriber to Camera
        self.cam_sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

    def camCallback(self, data):
        bridge = CvBridge()
        try:
            self.cv_img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)

        if self.test_status == "Running":
            self.addToVideo()   
        else:
            pass
    
    def startRecording(self,name):
        print("Starting again")
        self.video_name = name+'.avi'
        self.test_status = "Running"
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter(os.path.join(self.path,self.video_name), fourcc, 12, (1440,1080), 1)
        
    def addToVideo(self): 
        print("Adding image")
        self.out.write(self.cv_img) 

    def stopRecording(self):
        print("Releasing Video")
        self.test_status = "Stop"
        self.out.release()

    def deleteVideo(self):
        print("Deleting Video")
        try:
            os.remove(os.path.join(self.path,self.video_name))
        except:
            pass
    
