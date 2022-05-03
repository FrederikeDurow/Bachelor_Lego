#!/usr/bin/env python3
import rospy
import cv2
import sys
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError
from computer_vision.msg import ProjectInfo
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import DataFile

class tracker:

    def __init__(self):
        self.project_name = "Motion Tracker Test"                                                                        #NEEDS TO COME FROM USER
        self.file_name = None
        self.start_frame = None
        self.current_frame = None
        #self.testStarted = False
        self.nrOfLaps = None
        self.lapCounter = 0
        #self.rois = [[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7]]
        self.rois = []
        self.test_started = False
        
        #Create subscriber to Setup Node
        self.setupSub = rospy.Subscriber("Motion", ProjectInfo, self.setupCallback)

        #Create subscriber to camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.camCallback)


### SETUP #############################################################################################################
    def setupCallback(self, data):
        self.file_name = data.FileName
        self.rois = data.Rois                                                                                    
        self.setup_datafile()
        self.setupSub.unregister()
        self.start_test()
    
    def setup_datafile(self):
        header = ["Motion Tracking Test"]                                                                
        self.lapFile = DataFile.DataFile(self.file_name,header)

### STARTING ##########################################################################################################
    def start_test(self):
        self.start_frame = self.current_frame
        self.test_started = True
        #CALL TRACKER                                                        

### RUNNING ###########################################################################################################
    def camCallback(self,data):
        if self.test_started == True:
            bridge = CvBridge()
            try:
                self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
            except CvBridgeError as e:
                print(e)
                
            self.undistort()
            if self.current_frame is not None:
                cv2.imshow(self.project_name, self.current_frame)
                cv2.waitKey(10)

            self.get_data()
            self.process_data()

    def undistort(self):
        cMat = np.array([[1190.244030400389, 0, 729.660947406785],[0, 1183.894733755722, 562.2194095063451],[0, 0, 1]]) 
        dist = np.array([[-0.2364909197149232, 0.09037841331243952, -9.091405949805423e-05, 0.001536567533562297, 0]])
        self.current_frame = cv2.undistort(self.current_frame, cMat, dist, None)

    def get_data(self):
        #Get position from tracker
        return 1


    def process_data(self):
        #is position in lap-roi? 
            #if yes has it been there last frame? 
                #if yes, do nothing
                self.lapCounter += 1
            #if no, but has been last frame, reset 
        

### TEST DONE ##############################################################################################################
    def stop_test(self):
        #save video 
        self.save_data()
        print("The test has been completed and the data is saved.")
        #Stop all subscriptions, publisher and windows
        self.camSub.unregister()
        #self.roboSub.unregister()
        cv2.destroyAllWindows()

    def save_data(self):
        row = ['Nr of laps detected:', self.lapCounter]                                                             
        self.lapFile.save_data(row)
    

def main():
    m = tracker()
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass



class FeatureMatcher():

#     Algo = None
#     Matcher_obj = None
#     temp_img = None
#     test_img = None
#     cv_img = None

#     gray_temp_img = None
#     gray_test_img = None

#     keypts_1 = 0
#     descrip_1 = 0

#     keypts_2 = 0
#     descrip_2 = 0

#     matches = []
#     output_img = None
    
#     def __init__(self):
#         self.type = 'SIFT'
#         self.matcher = 'BFMATCHER'
#         self.Algo = cv2.SIFT_create() 
#         self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)
        
#     def callback(self,data):
#         bridge = CvBridge()
#         try:
#             self.cv_img = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
#         except CvBridgeError as e:
#             print(e)

#         #Convert color to gray scale
#         if self.cv_img.ndim == 3:
#                 self.cv_img = cv2.cvtColor(self.cv_img, cv2.COLOR_BGR2GRAY)
        
#         #If first frame
#         if self.temp_img is None:
#             self.temp_img = self.cv_img
#             cv2.imshow("temp", self.temp_img)
#             cv2.waitKey(10)

#         #if not first frame
#         elif cv2.waitKey(1) & 0xFF == 110: #if n is pressed
#             self.test_img = self.cv_img
#             cv2.imshow("ny", self.test_img)
#             cv2.waitKey(10)
#             self.applyDetector()
#             self.applyMatcher()
#             self.drawMatches(30)

#     def applyDetector(self): 
#         # Perform detection & computation based on parameters set
#         self.keypts_1, self.descrip_1 = self.Algo.detectAndCompute(self.temp_img, None)
#         self.keypts_2, self.descrip_2 = self.Algo.detectAndCompute(self.test_img, None)

#     def applyMatcher(self):
#         self.Matcher_obj = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
#         self.matches = self.Matcher_obj.match(self.descrip_1,self.descrip_2)
#         self.matches = sorted(self.matches, key= lambda match : match.distance)
#         print('SIFT & BFMATCHER selected')

      
#     def drawMatches(self, amount):
#         if self.matcher == 'BFMATCHER':
#             # add "flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS" if you dont wont points not used
#             self.output_img = cv2.drawMatches(self.temp_img, self.keypts_1, self.test_img, self.keypts_2, self.matches[:amount],None)
      
#         # resizes the image to 720p
#         self.output_img = cv2.resize(self.output_img, (1280,720))
#         cv2.imshow('Matches', self.output_img)
#         cv2.waitKey(0)