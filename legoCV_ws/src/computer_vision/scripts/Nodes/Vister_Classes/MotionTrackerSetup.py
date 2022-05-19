#!/usr/bin/env python3
import rospy
import cv2
import sys,os
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
#sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
import ROIs
from computer_vision.msg import MotionTrackerInfo
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
        self.path = None
        self.hsv_low = []
        self.hsv_up = []
        self.state = 0
        
        #Initializations for Regions of Interest
        self.newRois = ROIs.ROIs(self.windowName, self.current_frame)

        #Initialization of message
        self.msg = None
        self.trackbar = "Not Running"

        #Flags
        self.firstImage = 1
        self.createTrackbars = 0
        self.hsv_done = False
        self.cam_ready = False
        
        
    def callback(self, data):
        cv2.namedWindow(self.windowName,cv2.WINDOW_NORMAL)

        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
        except CvBridgeError as e:
            print(e)
        self.current_frame = self.newRois.draw_rois(self.current_frame)
        
        if self.trackbar == "Not Running":
            cv2.imshow(self.windowName, self.current_frame)
            cv2.waitKey(1)
            
        elif self.trackbar == "Running":
            self.set_HSV()

    def set_HSV(self):
        if self.createTrackbars == 1:
            # Create trackbars for color change
            # Hue is from 0-179 for Opencv
            cv2.createTrackbar('Hue_Min', self.windowName, 0, 179, nothing)
            cv2.createTrackbar('Sat_Min', self.windowName, 0, 255, nothing)
            cv2.createTrackbar('Val_Min', self.windowName, 0, 255, nothing)
            cv2.createTrackbar('Hue_Max', self.windowName, 0, 179, nothing)
            cv2.createTrackbar('Sat_Max', self.windowName, 0, 255, nothing)
            cv2.createTrackbar('Val_Max', self.windowName, 0, 255, nothing)

            # Set default value for Max HSV trackbars
            cv2.setTrackbarPos('Hue_Max', self.windowName, 179)
            cv2.setTrackbarPos('Sat_Max', self.windowName, 255)
            cv2.setTrackbarPos('Val_Max', self.windowName, 255)

            # Initialize HSV min/max values
            hMin = sMin = vMin = hMax = sMax = vMax = 0
            phMin = psMin = pvMin = phMax = psMax = pvMax = 0
            print("\n[USER INPUT] Press 's' to save chosen threshold")
            self.createTrackbars = 0
    
        else:
            hMin = cv2.getTrackbarPos('Hue_Min', self.windowName)
            sMin = cv2.getTrackbarPos('Sat_Min', self.windowName)
            vMin = cv2.getTrackbarPos('Val_Min', self.windowName)
            hMax = cv2.getTrackbarPos('Hue_Max', self.windowName)
            sMax = cv2.getTrackbarPos('Sat_Max', self.windowName)
            vMax = cv2.getTrackbarPos('Val_Max', self.windowName)

            # Set minimum and maximum HSV values to display
            self.HSV_lower = np.array([hMin, sMin, vMin])
            self.HSV_upper = np.array([hMax, sMax, vMax])

            # Convert to HSV format and color threshold
            hsv = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
            result = cv2.bitwise_and(self.current_frame, self.current_frame, mask=mask)

            # # Print if there is a change in HSV value
            # if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
            #     print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
            #     phMin = hMin
            #     psMin = sMin
            #     pvMin = vMin
            #     phMax = hMax
            #     psMax = sMax
            #     pvMax = vMax

            # Display result image
            self.current_frame = self.newRois.draw_rois(self.current_frame)
            cv2.imshow(self.windowName, result)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                self.trackbar = "Not running"
                self.hsv_low= [hMin, sMin, vMin]
                self.hsv_up = [hMax, sMax, vMax]
                cv2.destroyAllWindows()
                self.hsv_done = True
                self.publish_info()
                #break
            else:
                pass


    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]])
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)

    def set_test_info(self):
        self.set_laps()
        self.set_rois()
        self.set_path()
        self.set_file_name()
        self.trackbar = "Running"
        self.createTrackbars = 1
        

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

    def set_path(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = str(input())
       
    def set_file_name(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.fileName = input()

    def create_test_message(self):
        info = MotionTrackerInfo()
        info.FileName = self.fileName
        info.Lap = int(self.nrOfLaps)
        info.DataPath = self.path
        info.HSV_lower = self.hsv_low
        info.HSV_upper = self.hsv_up
        for i in range(len(self.rois)):
            rList = RoiList() 
            rList.RoiInfo = self.rois[i]
            info.Rois.append(rList)
        self.msg = info

    
    def publish_info(self):
        self.create_test_message()
        testPub = rospy.Publisher("MotionTracking", MotionTrackerInfo, queue_size=10)
        rate = rospy.Rate(10) #10Hz
        self.sub.unregister()
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()


def nothing(x):
    pass