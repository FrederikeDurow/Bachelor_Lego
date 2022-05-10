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
from Classes import Object_Color_Detector
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
        self.hsv_low = []
        self.hsv_up = []

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
        self.set_hsv_thresh()
        self.set_laps()
        self.set_rois()
        # self.set_color()
        self.set_file_name()
    
    def set_hsv_thresh(self):
        self.hsv_low, self.hsv_up = self.HSV_Trackbar()

    def set_laps(self):
        print("\n[USER INPUT] Please enter number of laps:")
        self.nrOfLaps = input()

    def get_laps(self):
        return self.nrOfLaps
    
    def set_rois(self):
        print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        self.newRois.set_single_roi()
        print("\n[USER INPUT] Choose where a lap starts/ends.")
        self.newRois.set_single_roi()
        self.rois = self.newRois.get_rois()
    
    def get_rois(self):
        return self.newRois.get_rois()
    
    # def set_color(self):
    #     print("\n[USER INPUT] What color should be tracked?\n'r' - red\n'b' - blue\n 'g' - green")
    #     while True:
    #         key = input()
    #         if key == "r" or key == "g" or key == "b":
    #             self.color = key
    #             break
    #         else:
    #             print("[MSG] The pressed key is not an option.")
        
    def set_file_name(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.fileName = input()

    def create_test_message(self):
        info = ProjectInfo()
        info.FileName = self.fileName
        info.Lap = int(self.nrOfLaps)
        #info.Color = self.color
        info.HSV_lower = self.hsv_low
        info.HSV_upper = self.hsv_up
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        self.msg = info

    
    def publish_info(self):
        self.create_test_message()
        testPub = rospy.Publisher("MotionTracking", ProjectInfo)
        rate = rospy.Rate(10) #10Hz
        self.sub.unregister()
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()


    def HSV_Trackbar(self):

        

        cv2.namedWindow('frame')

        # Create trackbars for color change
        # Hue is from 0-179 for Opencv
        cv2.createTrackbar('Hue_Min', 'frame', 0, 179, nothing)
        cv2.createTrackbar('Sat_Min', 'frame', 0, 255, nothing)
        cv2.createTrackbar('Val_Min', 'frame', 0, 255, nothing)
        cv2.createTrackbar('Hue_Max', 'frame', 0, 179, nothing)
        cv2.createTrackbar('Sat_Max', 'frame', 0, 255, nothing)
        cv2.createTrackbar('Val_Max', 'frame', 0, 255, nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('Hue_Max', 'frame', 179)
        cv2.setTrackbarPos('Sat_Max', 'frame', 255)
        cv2.setTrackbarPos('Val_Max', 'frame', 255)

        # Initialize HSV min/max values
        hMin = sMin = vMin = hMax = sMax = vMax = 0
        phMin = psMin = pvMin = phMax = psMax = pvMax = 0

        while(True):
            frame = self.current_frame
            if frame is not None:
                # Get current positions of all trackbars
                hMin = cv2.getTrackbarPos('Hue_Min', 'frame')
                sMin = cv2.getTrackbarPos('Sat_Min', 'frame')
                vMin = cv2.getTrackbarPos('Val_Min', 'frame')
                hMax = cv2.getTrackbarPos('Hue_Max', 'frame')
                sMax = cv2.getTrackbarPos('Sat_Max', 'frame')
                vMax = cv2.getTrackbarPos('Val_Max', 'frame')

                # Set minimum and maximum HSV values to display
                self.HSV_lower = np.array([hMin, sMin, vMin])
                self.HSV_upper = np.array([hMax, sMax, vMax])

                # Convert to HSV format and color threshold
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
                result = cv2.bitwise_and(frame, frame, mask=mask)

                # Print if there is a change in HSV value
                if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
                    print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
                    phMin = hMin
                    psMin = sMin
                    pvMin = vMin
                    phMax = hMax
                    psMax = sMax
                    pvMax = vMax

                # Display result image
                cv2.imshow('frame', result)
                print("\n[USER INPUT] Press 's' to save chosen threshold")
                # if key == "d":
                #     self.rois.pop()
                # elif key == "s":
                #     break
                if cv2.waitKey(10) & 0xFF == ord('s'):
                    cv2.destroyAllWindows()
                    return self.HSV_lower, self.HSV_upper

def nothing(x):
    pass