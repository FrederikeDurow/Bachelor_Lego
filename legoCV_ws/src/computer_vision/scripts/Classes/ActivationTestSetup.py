#!/usr/bin/env python3
import rospy
import cv2
import sys
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import Bool
from cv_bridge import CvBridge, CvBridgeError
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ROIs
from computer_vision.msg import ProjectInfo
from computer_vision.msg import RoiList

class ActivationTestSetup:

    def __init__(self):
        #Initializations for Camera Stream
        self.current_frame = None
        self.windowName = 'Camera Live Stream'
        
        self.sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.callback)

        #Initializations for Test Info
        self.testType = None
        self.nrOfLaps = 0
        self.fileName = None
        self.path = None
        self.rois = []
        self.testVideo = 0
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
        #cv2.namedWindow(self.windowName)
        cv2.imshow(self.windowName, self.current_frame)
        cv2.waitKey(10)

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)

    def set_test_info(self):
        self.set_laps()
        self.set_video_settings()
        self.set_path()
        self.set_file_name()
        self.set_rois()

    def set_laps(self):
        print("\n[USER INPUT] Please enter number of laps:")
        self.nrOfLaps = input()

    def get_laps(self):
        return self.nrOfLaps
    
    def set_rois(self):
        print("\n[USER INPUT] Choose all regions of interest.")
        self.newRois.set_multi_rois()
        self.rois = self.newRois.get_rois()
    
    def get_rois(self):
        return self.newRois.get_rois()

    def set_path(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = input()
    
    def set_file_name(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.fileName = input()
    
    def set_video_settings(self):
        print("\n[USER INPUT] Do you want to save a video of the whole test? (y/n)")
        self.testVideo = input()
        # print("\n[USER INPUT] Do you want to save a videos of malfunctions? (1 - yes, 0 - no)")
        # self.malfunctionVideo = input()

    def create_test_message(self):
        info = ProjectInfo()
        info.FileName = self.fileName
        info.Lap = int(self.nrOfLaps)
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        if self.testVideo == "y":
            info.TestVideo = True
        else:
            info.TestVideo = False
        info.DataPath = self.path
        self.msg = info
    
    def publish_info(self):
        self.create_test_message()
        testPub = rospy.Publisher("ActivationTest", ProjectInfo, queue_size=10)
        robotPub = rospy.Publisher("StartRobot", Bool, queue_size=10)
        rate = rospy.Rate(10) #10Hz
        self.sub.unregister()
        cv2.destroyWindow(self.windowName)
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            robotPub.publish(True)
            rate.sleep()
