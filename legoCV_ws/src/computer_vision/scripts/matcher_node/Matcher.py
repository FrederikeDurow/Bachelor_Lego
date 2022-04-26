#!/usr/bin/env python3
import rospy
import cv2 
import sys
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class Matcher():

    def __init__(self, rois):
        self.bridge = CvBridge()
        self.nrOfRois = rois
        self.current_frame = None
        
        self.create_subscriber()
        self.create_publisher()
        
    def get_currentFrame(self):
        return self.current_frame

    def create_subscriber(self):
        #Subscribe to camera image (CHANGE TO UNDISTORTED)
        self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)
        

    def create_publisher(self):
        self.pub = rospy.Publisher('LapOutcome', String, queue_size=self.nrOfRois)
        rospy.init_node('Matcher', anonymous=True)
        rate = rospy.Rate(10) #10Hz


    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "Camera Image recieved")
        try:
            self.current_frame = self.bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)
        self.undistort()



    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)