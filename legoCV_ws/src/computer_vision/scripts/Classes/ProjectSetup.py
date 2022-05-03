#!/usr/bin/env python3
import rospy
import cv2
import sys
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import ROIs
from computer_vision.msg import ProjectInfo
from computer_vision.msg import RoiList

class ProjectSetup:

    def __init__(self, name):

        #Initializations for Camera Stream
        self.current_frame = None
        self.windowName = name
        self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)


        #Initializations for Test Info
        self.testType = None
        self.nrOfLaps = 0
        self.fileName = None
        self.rois = []
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
            
        self.undistort()
        self.current_frame = self.newRois.draw_rois(self.current_frame)
        cv2.imshow(self.windowName, self.current_frame)
        cv2.waitKey(10)

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)

    def set_test_type(self):
        print("What test do you want to run?")
        print("Press 'a' for an Activation Test or 'm' for a Motion Tracking Test, followed by pressing enter")
        while True:
            key = input()
            if key == "a":
                self.testType = "ActivationTestInfo"
                break
            elif key == "m":
                self.testType = "MotionTrackingInfo"
                break


    def set_test_info(self):
        self.set_test_type()
        self.set_laps()
        self.set_rois()
        self.set_file_name()

    def get_test_type(self):
        return self.testType

    def set_laps(self):
        print("Please enter number of laps, followed by pressing enter.")
        self.nrOfLaps = input()

    def get_laps(self):
        return self.nrOfLaps
    
    def set_rois(self):
        self.newRois.set_rois()
        self.rois = self.newRois.get_rois()

    def get_rois(self):
        return self.newRois.get_rois()
    
    def set_file_name(self):
        print("Please enter the output file name, followed by pressing enter:")
        self.fileName = input()

    def create_message(self):
        info = ProjectInfo()
        info.FileName = self.fileName
        info.Lap = int(self.nrOfLaps)
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        self.msg = info
        print(self.msg)
    
    def publish_info(self):
        pub = rospy.Publisher(self.testType, ProjectInfo)
        rate = rospy.Rate(10) #10Hz
        #rospy.loginfo("Setup Node is publishing project information now")
        while not rospy.is_shutdown():
            pub.publish(self.msg)
            rate.sleep()