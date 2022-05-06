#!/usr/bin/env python3
from matplotlib.pyplot import draw
import rospy
import sys
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import MotionTrackerTest


def main():
    rospy.init_node('MotionTracker', anonymous=True)
    M = MotionTrackerTest.MotionTracker()
    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
