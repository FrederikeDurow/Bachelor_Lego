#!/usr/bin/env python3
import rospy
import cv2
import os
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class VideoSaver:

    def __init__(self, fileName, path):
        self.cvimg = None
        self.path = path
        self.testStatus = "Waiting"
        self.name = fileName+".avi"
        self.text = " "
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        #Create subscriber to Camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

        #Create Video Writer
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter(os.path.join(self.path,self.name), fourcc, 24, (1440,1080),1)
      

    def camCallback(self, data):
        if self.testStatus == "Running":
            bridge = CvBridge()
            try:
                self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
            except CvBridgeError as e:
                print(e)
            self.add_text()
            self.add_to_video()

        elif self.testStatus == "Stop":
            self.stop_recording()
        else:
            pass

    def cv_show(self):
        cv2.imshow("VideoSaver image", self.cvimg)
        cv2.waitKey(10)

    def start_recording(self):
        self.testStatus = "Running"
    
    def change_text(self, newText):
        self.text = newText
    
    def add_text(self):
        self.cvimg = cv2.putText(self.cvimg, self.text, (50,50), self.font, 1, (0,0,255),2, cv2.LINE_4)
    
    def stop_recording(self):
        self.testStatus = "Stop"
        self.out.release()

    def add_to_video(self): 
        self.out.write(self.cvimg)    
    
  
        