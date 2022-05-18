#!/usr/bin/env python3
from matplotlib.pyplot import draw
import rospy
import cv2
import sys,os
import time
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from computer_vision.msg import MotionTrackerInfo
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Vister_Classes'))
#sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
import DataFile
import Object_Color_Detector
import CentroidTracker
import VideoSaver
from collections import OrderedDict


class MotionTracker:

    def __init__(self):
        self.project_name = "Motion Tracker Test"                                                                        #NEEDS TO COME FROM USER
        self.file_name = None
        self.start_frame = None
        self.current_frame = None
        self.nrOfLaps = None
        self.lapCounter = 0
        self.total_roi = []
        self.lap_roi = []
        self.test_started = False
        self.H= None
        self.W= None
        self.detections = []
        self.crop_img = None
        self.objects = OrderedDict()
        self.path = None

        #For Tracker
        self.position = True
        self.old_position = True
        self.timer_started = False
        self.test_start_time = 0
        self.lap_start_time = 0
        self.lap_time = 0
        self.color = None

        #Create subscriber to Setup Node
        self.setupSub = rospy.Subscriber("MotionTracking", MotionTrackerInfo, self.setupCallback)

        #Create subscriber to camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

        #create Centroid Tracker
        self.tracker = CentroidTracker.centroidTracker()
        self.detector = Object_Color_Detector.obj_color_dectector()

### SETUP #############################################################################################################
    def setupCallback(self, data):
        self.unpack_message(data)
        self.setupSub.unregister()
        print("\n[MSG] Setup is completed.")
        self.start_test()
        
    def unpack_message(self, data):
        self.file_name = data.FileName
        self.nrOfLaps = data.Lap
        self.path = data.DataPath
        self.hsv_low = data.HSV_lower
        self.hsv_up = data.HSV_upper
        cnt = 0
        for roi in data.Rois:
            temp_roi = []
            for element in range(len(roi.RoiInfo)):
                temp_roi.append(roi.RoiInfo[element])
            if cnt == 0:
                self.total_roi = temp_roi
                cnt = 1
            elif cnt == 1: 
                self.lap_roi = [temp_roi[0]-self.total_roi[0],temp_roi[1]-self.total_roi[1], temp_roi[2], temp_roi[3]] 

    def start_test(self):
        self.VS = VideoSaver.VideoSaver(self.file_name, self.path)
        self.VS.start_recording()
        self.setup_datafile()
        self.update_timer()
        self.test_started = True
        print("\n[MSG] Test is running, don't shutdown computer.")  

    def setup_datafile(self):
        # header = ["Motion Tracking Test", "Lap", "Time pr Lap"]                                                                
        # self.lapFile = DataFile.DataFile(self.file_name,self.path,header)
        header = ["Motion Tracking Test", "Lap", "Time pr Lap"]                                                                
        self.lapFile = DataFile.DataFile(self.file_name,self.path,header)

### STARTING ##########################################################################################################
    # def start_test(self):
    #     self.test_started = True
    #     #CALL TRACKER                                                        

### RUNNING ###########################################################################################################
    def camCallback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        except CvBridgeError as e:
            print(e)
        if self.test_started == True and self.current_frame is not None:
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                self.stop_test()
            self.prep_image()
            
            self.detections = self.detector.applyColorDectector(self.crop_img, self.hsv_low, self.hsv_up, 200)
            self.objects = self.tracker.update(self.detections)
            self.draw_id()
            cv2.rectangle(self.crop_img, (self.lap_roi[0],self.lap_roi[1]), (self.lap_roi[0]+self.lap_roi[2], self.lap_roi[1]+self.lap_roi[3]), (0,255,0), 2)
            cv2.imshow(self.project_name, self.crop_img)
            self.check_position()
            self.update_laps()
            
            if self.lapCounter == self.nrOfLaps:
                self.stop_test()


    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]]) 
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)
        
    def prep_image(self):
        blurred = cv2.GaussianBlur(self.current_frame, (11, 11), 0)
        self.crop_img = blurred[self.total_roi[1] : self.total_roi[1]+self.total_roi[3], self.total_roi[0] : self.total_roi[0]+self.total_roi[2]]

         

    def draw_detections(self):
        if  self.detections is not None:
            for i in range(len(self.detections)):
                (startX, startY, endX, endY,_) = self.detections[i]
                cv2.rectangle(self.crop_img, (startX,startY), (startX+endX, startY+endY), (0,255,0), 2)

    def draw_id(self):
        if self.objects is not None:
            for (objectID, centroid) in self.objects.items():
                text = "ID {}".format(objectID)
                cv2.putText(self.crop_img, text, (centroid[0]-10, centroid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
                cv2.circle(self.crop_img, (centroid[0], centroid[1]), 4, (0,0,255), -1)

  
    def check_position(self):
        self.old_position = self.position
        if self.objects is not None:
            for (objectID, centroid) in self.objects.items():                                                           #FIX: WE NEED TO MAKE SURE WE ONLY HAVE ONE OBJECT
                if centroid[0] in range(self.lap_roi[0],self.lap_roi[0]+self.lap_roi[2]):
                    if centroid[1] in range(self.lap_roi[1],self.lap_roi[1]+self.lap_roi[3]):
                        self.position = True
                    else:
                        self.position = False
                else: 
                    self.position = False
        
    def update_laps(self):
        if self.old_position == False and self.position == True:
            self.lapCounter += 1
            self.update_timer()
            self.save_data()
            sys.stdout.write("\r")
            sys.stdout.write("\n{:3d} laps done." .format(self.lapCounter))
            sys.stdout.flush()
        

    def update_timer(self):
        if self.timer_started == False:
            self.timer_started = True
            self.test_start_time = time.time()
            self.lap_start_time = time.time()
        self.lap_time = time.time() - self.lap_start_time
        self.lap_start_time = time.time()
       
### TEST DONE ##############################################################################################################
    def stop_test(self):
        self.VS.stop_recording()
        print("\n[MSG] The test has been completed and the data is saved.")
        self.camSub.unregister()
        cv2.destroyAllWindows()

    def save_data(self):
        row = ['', self.lapCounter, self.lap_time]                                                             
        self.lapFile.save_data(row)
        if self.lapCounter == self.nrOfLaps:
            row = ['', "Total Time: ", time.time()-self.test_start_time]                                                             
            self.lapFile.save_data(row)