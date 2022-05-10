#!/usr/bin/env python3
import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

cap = cv2.VideoCapture("/home/frederike/Desktop/Lap3.avi")
#cap = cv2.VideoCapture("/home/frederike/.ros/tester.avi")


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("test", frame)

