#!/usr/bin/env python3
import rospy
import sys
import cv2


#sys.path.insert(0, 'C:/LEGO/Bachelor_Lego')
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts/matcher_node')
from activation_node import BoundingBox 
from activation_node import Test_Setup





def main():
    rospy.init_node('ActivationTest', anonymous=True)
    at = Test_Setup()

    rospy.spin()

    bBox = BoundingBox.BoundingBox()
    bBox.applyBoundingBox(at.current_frame)
    

if __name__ == '__main__':
    main()









