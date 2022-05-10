#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class VideoSaver:

    def __init__(self, fileName):
        self.cvimg = None
        self.testStatus = "Waiting"

        #Create subscriber to Camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

        #Create Video Writer
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter(fileName+'.avi', fourcc, 24, (1440,1080), 1)

    def camCallback(self, data):
        if self.testStatus == "Running":
            bridge = CvBridge()
            try:
                self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
            except CvBridgeError as e:
                print(e)
            self.save_video()

        elif self.testStatus == "Done":
            self.stream_closed()
        else:
            pass

    def cv_show(self):
        cv2.imshow("cv image", self.cvimg)
        cv2.waitKey(10)
    
    def start_recording(self):
        self.testStatus = "Running"
    
    def stop_recording(self):
        self.testStatus = "Done"

    def save_video(self): 
        self.out.write(self.cvimg)    
    
    def stream_closed(self):
        self.out.release()