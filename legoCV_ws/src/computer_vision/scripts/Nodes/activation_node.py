#!/usr/bin/env python3
import rospy
import sys,os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
# sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Vister_Classes import ActivationTest
    
def main():
    rospy.init_node('ActivationTest', anonymous=True)
    at = ActivationTest.ActivationTest()
    rospy.spin()
    
if __name__ == '__main__': 
    main()









