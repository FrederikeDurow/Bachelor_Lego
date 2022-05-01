#!/usr/bin/env python3
import rospy
import sys
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class activation_test:

    def __init__(self):
        self.current_frame

        #Create subscriber to camera
        camSub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.camCallback)

        #Create subscriber to Setup Node
        setupSub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.setupCallback)

    def camCallback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        except CvBridgeError as e:
            print(e)
            
        self.undistort()
        cv2.imshow('Camera Live Stream', self.current_frame)
        cv2.waitKey(10)

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)
