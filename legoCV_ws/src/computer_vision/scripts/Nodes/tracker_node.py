#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class tracker:

    def __init__(self, rois):
        self.nrOfRois = rois
        
        #Subscribe to camera image (CHANGE TO UNDISTORTED)
        self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)

        self.pub = rospy.Publisher('LapOutcome', String, queue_size=self.nrOfRois)
        rospy.init_node('Matcher', anonymous=True)
        rate = rospy.Rate(10) #10Hz
        
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            rate.sleep()

    def callback(self, data):
        bridge = CvBridge()
        rospy.loginfo(rospy.get_caller_id() + "Camera Image recieved")
        try:
            self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)
    
    def publish_data(self):
        

def main():
    m = tracker(10)
    
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
