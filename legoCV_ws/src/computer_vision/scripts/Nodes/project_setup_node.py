#!/usr/bin/env python3
import rospy
import sys
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ActivationTestSetup
from Classes import MotionTrackerSetup

def choose_test():
    while True:
        print("\n[USER INPUT] Choose one of the following tests:\n'a' - Activation Test \n'm' - Motion Tracking Test")
        key = input()
        if key == "a" or key == "m":
            return key
            
def main():
    rospy.init_node('Setup', anonymous=True)
    test = choose_test()
    if test == "a":
        newProject = ActivationTestSetup.ActivationTestSetup()
    else:
        newProject = MotionTrackerSetup.MotionTrackerSetup()
    newProject.set_test_info()
    newProject.publish_info()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
