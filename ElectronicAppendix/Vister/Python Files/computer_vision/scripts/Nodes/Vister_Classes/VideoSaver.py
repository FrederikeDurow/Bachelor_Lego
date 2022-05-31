#!/usr/bin/env python3
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class VideoSaver:

    def __init__(self, fileName, path):
        self.cv_img = None
        self.path = path
        self.test_status = "Waiting"
        self.name = fileName+".avi"
        self.text = " "
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        #Create subscriber to Camera
        self.cam_sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

        #Create Video Writer
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter(os.path.join(self.path,self.name), fourcc, 24, (1440,1080),1)
      

    def camCallback(self, data):
        if self.test_status == "Running":
            bridge = CvBridge()
            try:
                self.cv_img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
            except CvBridgeError as e:
                print(e)
            self.addText()
            self.addToVideo()

        elif self.test_status == "Stop":
            self.stopRecording()
        else:
            pass

    def startRecording(self):
        self.test_status = "Running"
    
    def changeText(self, newText):
        self.text = newText
    
    def addText(self):
        self.cv_img = cv2.putText(self.cv_img, self.text, (50,50), self.font, 1, (0,0,255),2, cv2.LINE_4)
    
    def stopRecording(self):
        self.test_status = "Stop"
        self.out.release()

    def addToVideo(self): 
        self.out.write(self.cv_img)    
    
  
        