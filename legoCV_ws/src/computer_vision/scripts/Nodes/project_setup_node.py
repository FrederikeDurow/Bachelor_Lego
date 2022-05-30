#!/usr/bin/env python3
import os
import sys

import rospy

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
from Vister_Classes import (ActivationTestSetup, LiveMotionTrackerSetup,
                            VideoMotionTrackerSetup)


def choose_test():
    print("\n[USER INPUT] Choose one of the following tests:\n'a' - Activation Test \n'vm' - Video Motion Tracking Test\n'lm' - Live Motion Tracking Test ")
    while True:
        key = input()
        if key == "a" or key == "vm" or key == "lm":
            return key
            
def main():
    rospy.init_node('Setup', anonymous=True)
    test = choose_test()
    if test == "a":
        newProject = ActivationTestSetup.ActivationTestSetup()
    elif test == "vm":
        newProject = VideoMotionTrackerSetup.MotionTrackerSetup()
    elif test == "lm":
        newProject = LiveMotionTrackerSetup.MotionTrackerSetup()
    newProject.set_test_info()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
