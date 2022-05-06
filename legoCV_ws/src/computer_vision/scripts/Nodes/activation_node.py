#!/usr/bin/env python3
import rospy
import sys
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ActivationTest

def main():
    rospy.init_node('ActivationTest', anonymous=True)
    at = ActivationTest.ActivationTest()
    rospy.spin()
    
if __name__ == '__main__':
    main()









