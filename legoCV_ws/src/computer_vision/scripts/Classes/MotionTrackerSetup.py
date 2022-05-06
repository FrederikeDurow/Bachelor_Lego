#!/usr/bin/env python3
import rospy
import cv2
import sys
import numpy as np
import subprocess
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge, CvBridgeError
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ROIs
from computer_vision.msg import ProjectInfo
from computer_vision.msg import RoiList

class MotionTrackerSetup:

    def __init__(self):
        #Initializations for Camera Stream
        self.current_frame = None
        self.windowName = "Motion Tracker Test"
        self.sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.callback)

        #Initializations for Test Info
        self.nrOfLaps = 0
        self.fileName = None
        self.rois = []
        self.color = None

        #Initializations for Regions of Interest
        self.newRois = ROIs.ROIs(self.windowName, self.current_frame)

        #Initialization of message
        self.msg = None
        

    def callback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        except CvBridgeError as e:
            print(e)
        self.current_frame = self.newRois.draw_rois(self.current_frame)
        cv2.namedWindow(self.windowName)
        cv2.imshow(self.windowName, self.current_frame)
        cv2.waitKey(10)

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)

    def set_test_info(self):
        self.set_laps()
        self.set_rois()
        self.set_color()
        self.set_file_name()
    

    def set_laps(self):
        print("[WAIT USER] Please enter number of laps:")
        self.nrOfLaps = input()

    def get_laps(self):
        return self.nrOfLaps
    
    def set_rois(self):
        print("[WAIT USER] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        self.newRois.set_single_roi()
        print("[WAIT USER] Choose where a lap starts/ends.")
        self.newRois.set_single_roi()
        self.rois = self.newRois.get_rois()
    
    def get_rois(self):
        return self.newRois.get_rois()
    
    def set_color(self):
        print("[WAIT USER] Is the object to track red, blue or green? Type 'r', 'b' or 'g':")
        while True:
            key = input()
            if key == "r" or key == "g" or key == "b":
                self.color = key
                break
            else:
                pass
        
    def set_file_name(self):
        print("[WAIT USER] Please enter the output file name:")
        self.fileName = input()

    def create_test_message(self):
        info = ProjectInfo()
        info.FileName = self.fileName
        info.Lap = int(self.nrOfLaps)
        info.Color = self.color
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        self.msg = info
        print(self.msg)
    
    def publish_info(self):
        self.create_test_message()
        testPub = rospy.Publisher("MotionTracking", ProjectInfo)
        rate = rospy.Rate(10) #10Hz
        self.sub.unregister()
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()
