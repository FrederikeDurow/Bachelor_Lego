#!/usr/bin/env python3
import rospy
import sys

#sys.path.insert(0, 'C:/LEGO/Bachelor_Lego')
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts/matcher_node')
from matcher_node import BoundingBox 
from matcher_node import Matcher 

def main():
    rospy.init_node('Matcher', anonymous=True)
    rospy.spin()
    
    matcher = Matcher(2)
    bBox = BoundingBox.BoundingBox()
    bBox.applyBoundingBox(matcher.current_frame)
    

if __name__ == '__main__':
    main()









