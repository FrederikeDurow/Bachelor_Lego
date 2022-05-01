#!/usr/bin/env python3
from cv2 import imshow
from numpy import empty
import rospy
import sys
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

#sys.path.insert(0, 'C:/LEGO/Bachelor_Lego')
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import BoundingBox 
from Classes import ActivationTest


def main():

    rospy.init_node('ActivationTest', anonymous=True)

    at = ActivationTest.ActivationTest("Activation Test")
    # if at.get_current_frame() is not None:
    #     imshow("hey", at.get_current_frame())
    #     cv2.waitKey(0)
    rospy.spin()

    # bBox = BoundingBox.BoundingBox()
    # bBox.applyBoundingBox(at.current_frame)
    

if __name__ == '__main__':
    main()









