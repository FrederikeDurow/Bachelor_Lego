#!/usr/bin/env python3
from cv2 import VideoCapture
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
        self.initial_frame = None
        self.window_name = "Motion Tracker Test"
        
        #self.sub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.callback)
        
        #Initializations for Test Info
        #self.nrOfLaps = 0
        self.video_path = None
        self.file_name = None
        self.rois = []
        self.path = None
        self.hsv_low = []
        self.hsv_up = []
        self.state = 0
        
        self.new_rois = ROIs.ROIs(self.window_name)

        #Initialization of message
        self.msg = None
        self.trackbar = "Not Running"

        #Flags
        self.first_image = 1
        self.create_trackbars = 0
        self.hsv_done = False
        self.cam_ready = False

        #Kun til ROI
        self.temp_roi = []
        self.rois = []
        self.roi_state = 0
        self.roi_added = 0
        self.roi_chosen = False
        
        
    # def callback(self, data):
    #     cv2.namedWindow(self.windowName,cv2.WINDOW_NORMAL)

    #     bridge = CvBridge()
    #     try:
    #         self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='bgr8')
    #     except CvBridgeError as e:
    #         print(e)
    #     self.current_frame = self.newRois.draw_rois(self.current_frame)
        
    #     if self.trackbar == "Not Running":
    #         cv2.imshow(self.windowName, self.current_frame)
    #         cv2.waitKey(1)
            
    #     elif self.trackbar == "Running":
    #         self.set_HSV()



    def set_test_info(self):
        #self.set_laps()
        self.get_video()
        #self.open_video()
        self.set_rois()
        self.set_path()
        self.set_file_name()
        self.trackbar = "Running"
        self.create_trackbars = 1
        self.set_HSV()
        print("færdig med test info")
        

    def get_video(self):
        print("\n[USER INPUT] Please enter the path to the video:")
        self.video_path = input()
    
    # def open_video(self):
    #     cap = cv2.VideoCapture(self.video_path)
    #     ret, self.initial_frame = cap.read()
    #     if ret:
    #         cv2.namedWindow(self.window_name)
    #         cv2.imshow(self.window_name, self.initial_frame)
    #         cv2.waitKey(0)
    #     else:
    #         print("[WARNING] Could not open video")

    # def set_laps(self):
    #     print("\n[USER INPUT] Please enter number of laps:")
    #     self.nrOfLaps = input()

    # def get_laps(self):
    #     return self.nrOfLaps
    
    # def set_rois(self):
    #     #Initializations for Regions of Interest
    #     cv2.namedWindow(self.window_name)
    #     cap = cv2.VideoCapture(self.video_path)
    #     ret, self.initial_frame = cap.read()
    #     if ret:
    #         cv2.imshow(self.window_name, self.initial_frame)
    #         cv2.waitKey(10)
        
    #     print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
    #     self.new_rois.set_single_roi()
    #     print("\n[USER INPUT] Choose where a lap starts/ends.")
    #     self.new_rois.set_single_roi()
    #     self.rois = self.new_rois.get_rois()

    def set_rois(self):
        cap = cv2.VideoCapture(self.video_path)
        ret, self.initial_frame = cap.read()
        #Initializations for Regions of Interest
        print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        roi = cv2.selectROI(self.initial_frame)
        self.rois.append(roi)
        print("\n[USER INPUT] Choose where a lap starts/ends.")
        roi = cv2.selectROI(self.initial_frame)
        self.rois.append(roi)
        #cv2.setMouseCallback(self.window_name, self.add_roi)
        # roiCnt = 0
        # while roiCnt < 2 : 
        #     cv2.imshow(self.window_name, self.initial_frame)
        #     k = cv2.waitKey(0)
        #     print("\n[USER INPUT] Do you want to:\n'd' - delete last region\n's' - save chosen region\n")
        #     if k == ord("d"):
        #         self.rois.pop()
        #     elif k == ord("s"):
        #         roiCnt += 1
        #     else:
        #         print("[MSG] The pressed key is not an option.")
        
        # print("\n[USER INPUT] Choose the general region in which the object can be tracked (cut off unnecessary background).")
        # cv2.setMouseCallback(self.window_name, self.add_roi)
        # while True: 
        #     if self.roi_chosen == True:
        #         key = input("\n[USER INPUT] Do you want to:\n'd' - delete last region\n's' - save chosen region\n")
        #         if key == "d":
        #             self.rois.pop()
        #         elif key == "s":
        #             break
        #         else:
        #             print("[MSG] The pressed key is not an option.")
        # print("\n[USER INPUT] Choose where a lap starts/ends.")
        # cv2.setMouseCallback(self.window_name, self.add_roi)
        # while True: 
        #     if self.roi_chosen == True:
        #         key = input("\n[USER INPUT] Do you want to:\n'd' - delete last region\n's' - save chosen region\n")
        #         if key == "d":
        #             self.rois.pop()
        #         elif key == "s":
        #             break
        #         else:
        #             print("[MSG] The pressed key is not an option.")
        # self.rois = self.new_rois.get_rois()
    
    def add_roi(self, event,x,y,flags,*params):
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.set_upperleft(x,y)   
        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            self.set_lowerright(x,y)
        else: 
            pass

    def set_upperleft(self, x, y):
        self.temp_roi = []
        self.temp_roi.append(x)
        self.temp_roi.append(y)
        self.roi_chosen = True
        self.roi_state = 1
        pass


    def set_lowerright(self, x, y):
        self.temp_roi.append(x-self.temp_roi[0])
        self.temp_roi.append(y-self.temp_roi[1])
        self.rois.append(self.temp_roi)
        self.roi_state = 0
        self.roi_added = 1 
        pass



    def get_rois(self):
        return self.new_rois.get_rois()

    def set_path(self):
        print("\n[USER INPUT] Enter the location at which all data and video files should be saved.:")
        self.path = str(input())
       
    def set_file_name(self):
        print("\n[USER INPUT] Please enter the output file name:")
        self.file_name = input()

    def create_test_message(self):
        info = MotionTrackerInfo()
        info.VideoPath = self.video_path
        info.FileName = self.file_name
        #info.Lap = int(self.nrOfLaps)
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
        testPub = rospy.Publisher("VideoMotionTracking", MotionTrackerInfo, queue_size=10)
        rate = rospy.Rate(10) #10Hz
        #self.sub.unregister()
        while not rospy.is_shutdown():
            testPub.publish(self.msg)
            rate.sleep()
    
    def set_HSV(self):
        print("hej")
        cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)
        cv2.imshow(self.window_name, self.initial_frame)
        cv2.waitKey(1)
        
        #if self.create_trackbars == 1:
        # Create trackbars for color change
        # Hue is from 0-179 for Opencv
        cv2.createTrackbar('Hue_Min', self.window_name, 0, 179, nothing)
        cv2.createTrackbar('Sat_Min', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Val_Min', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Hue_Max', self.window_name, 0, 179, nothing)
        cv2.createTrackbar('Sat_Max', self.window_name, 0, 255, nothing)
        cv2.createTrackbar('Val_Max', self.window_name, 0, 255, nothing)

        # Set default value for Max HSV trackbars
        cv2.setTrackbarPos('Hue_Max', self.window_name, 179)
        cv2.setTrackbarPos('Sat_Max', self.window_name, 255)
        cv2.setTrackbarPos('Val_Max', self.window_name, 255)

        # Initialize HSV min/max values
        hMin = sMin = vMin = hMax = sMax = vMax = 0
        phMin = psMin = pvMin = phMax = psMax = pvMax = 0
        print("\n[USER INPUT] Press 's' to save chosen threshold")
        self.create_trackbars = 0
    
        while True:
            hMin = cv2.getTrackbarPos('Hue_Min', self.window_name)
            sMin = cv2.getTrackbarPos('Sat_Min', self.window_name)
            vMin = cv2.getTrackbarPos('Val_Min', self.window_name)
            hMax = cv2.getTrackbarPos('Hue_Max', self.window_name)
            sMax = cv2.getTrackbarPos('Sat_Max', self.window_name)
            vMax = cv2.getTrackbarPos('Val_Max', self.window_name)

            # Set minimum and maximum HSV values to display
            self.HSV_lower = np.array([hMin, sMin, vMin])
            self.HSV_upper = np.array([hMax, sMax, vMax])

            # Convert to HSV format and color threshold
            hsv = cv2.cvtColor(self.initial_frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
            result = cv2.bitwise_and(self.initial_frame, self.initial_frame, mask=mask)

            # Display result image
            self.initial_frame = self.new_rois.draw_rois(self.initial_frame)
            cv2.imshow(self.window_name, result)

            k = cv2.waitKey(1) & 0xFF
            if k == ord('s'):
                self.trackbar = "Not running"
                self.hsv_low= [hMin, sMin, vMin]
                self.hsv_up = [hMax, sMax, vMax]
                cv2.destroyAllWindows()
                self.hsv_done = True
                self.publish_info()
                break
            else:
                pass


def nothing(x):
    pass