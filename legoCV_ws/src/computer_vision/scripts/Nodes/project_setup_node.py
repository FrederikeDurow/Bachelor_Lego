#!/usr/bin/env python3
import rospy
import cv2
import sys
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ProjectSetup
from Classes import ROIs
from computer_vision.msg import ProjectInfo
from computer_vision.msg import RoiList

# def publish_info(testType, msg):
#         pub = rospy.Publisher(testType, ProjectInfo)
#         rate = rospy.Rate(10) #10Hz
#         rospy.loginfo("Setup Node is publishing project information now")
#         while not rospy.is_shutdown():
#             pub.publish(msg)
#             rate.sleep()

# def create_message(lap, rois):
#     info = ProjectInfo()
#     info.Lap = int(lap)
#     for i in range(len(rois)):
#         rList = RoiList() 
#         rList.Roi = rois[i]
#         info.Rois.append(rList)
#     return info

def main():
    windowName = 'Camera Live Stream'
    rospy.init_node('setup', anonymous=True)
    
    newProject = ProjectSetup.ProjectSetup(windowName)
    newProject.set_test_info()
    newProject.create_message()
    newProject.publish_info()
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
