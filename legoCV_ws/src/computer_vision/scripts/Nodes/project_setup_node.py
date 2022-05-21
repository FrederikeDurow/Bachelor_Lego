#!/usr/bin/env python3
import rospy
import sys,os
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
# sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Vister_Classes import ActivationTestSetup
from Vister_Classes import VideoMotionTrackerSetup
from Vister_Classes import LiveMotionTrackerSetup

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
    #newProject.publish_info()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
