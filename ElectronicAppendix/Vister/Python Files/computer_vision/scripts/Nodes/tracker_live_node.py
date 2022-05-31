#!/usr/bin/env python3
import os
import sys

import rospy

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
from Vister_Classes import LiveMotionTrackerTest


def main():
    rospy.init_node('MotionTracker', anonymous=True)
    LiveMotionTrackerTest.MotionTracker()
    rospy.spin()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
