#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class setup:

    def __init__(self):

        #Initializations for Camera Stream
        self.current_frame = None
        self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)
        self.rRun = True

        #Test Info
        self.testType = None
        self.rois = []
    

    def callback(self,data):
        if self.rRun is True:
            bridge = CvBridge()
            try:
                self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
            except CvBridgeError as e:
                print(e)
        
            #cv2.namedWindow('Camera Live Stream')
            cv2.imshow('Camera Live Stream', self.current_frame)
            cv2.waitKey(10)
    

    def choose_test(self):
        #rospy.sleep()
        print("What test do you want to run?")
        print("Press 'a' for an Activation Test or 'm' for a Motion Tracking Test, followed by pressing enter")
        while True:
            key = input()
            if key == "a":
                self.testType = "Activation"
                break
            elif key == "m":
                self.testType = "Motion Tracking"
                break
        print(self.testType)
        
    
    def choose_rois(self):
        print("rois")
        self.rRun = False
        while True:
            roi = cv2.selectROI('SelectRoi', self.current_frame)
            self.rois.append(roi)
        
            self.draw_rois()
            print("Press 's' to start tracking")
            print("Press 'd' to delete the last ROI")
            print("Press any other key to select the next object")
            break

            
    def draw_rois(self):
        for roi in self.rois:
            cv2.rectangle(self.current_frame, (roi[0], roi[1]), (roi[0]+roi[2] , roi[1]+roi[3]), (0,255,0), 2)
            
    

    def publish_data(self):
        self.pub = rospy.Publisher('NrOfRois', String, queue_size=self.nrOfRois)
        
        rate = rospy.Rate(10) #10Hz
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            rate.sleep()
        return 0

def main():
    rospy.init_node('setup', anonymous=True)
    newProject = setup()
    newProject.choose_test()
    newProject.choose_rois()
    rospy.spin()
    
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
