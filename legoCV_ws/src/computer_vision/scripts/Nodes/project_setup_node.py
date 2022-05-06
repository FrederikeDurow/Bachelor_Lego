#!/usr/bin/env python3
import rospy
import sys
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ProjectSetup

def main():
    windowName = 'Camera Live Stream'
    rospy.init_node('setup', anonymous=True)
    
    newProject = ProjectSetup.ProjectSetup(windowName)
    newProject.set_test_info()
    newProject.publish_info()
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
