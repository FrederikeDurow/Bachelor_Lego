#!/usr/bin/env python3
from matplotlib.pyplot import draw
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
 

        #Initializations for Test Info
        self.testType = None

        #Initializations for Regions of Interest
        print("setup")
        self.temp_roi = []
        self.rois = []
        self.roi_state = 0
        self.roi_added = 0

    def callback(self,data):
        bridge = CvBridge()
        try:
            self.current_frame = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')
        except CvBridgeError as e:
            print(e)

        #cv2.namedWindow('Camera Live Stream')
        self.draw_rois()
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
        print("Select a new ROI by clicking on its desired upper left corner and lower right corner position")
        while True:
            if self.roi_added == 0:

                cv2.setMouseCallback('Camera Live Stream', self.add_roi)
            else:
                print("Press 'd' to delete the last ROI")
                print("Press 'r' to select another ROI")
                print("Press any other key to select the next object")

                key = input()
                if key == "d":
                    self.rois.pop()
                elif key == "r":
                    self.roi_added = 0
                else:
                    break

    def add_roi(self, event ,x,y,flags,params):
        
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.temp_roi = []
            self.temp_roi.append(x)
            self.temp_roi.append(y)
            self.roi_state = 1
            
           
        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            self.temp_roi.append(x-self.temp_roi[0])
            self.temp_roi.append(y-self.temp_roi[1])
            self.rois.append(self.temp_roi)
            self.roi_state = 0
            self.roi_added = 1 


    def draw_rois(self):
        self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_GRAY2BGR)

        if len(self.temp_roi) > 0:
            cv2.circle(self.current_frame, (self.temp_roi[0],self.temp_roi[1]), 2, (0,255,0), -1)

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




# def choose_rois(self):
#        done = False

#        while done == False:
#             rospy.sleep(1000)
#             roi = cv2.selectROI('Camera Live Stream',self.current_frame)
            
#             print("Press 'd' to delete the last ROI")
#             print("Press 's' to save the chosen ROIs ")
            

#             key = input()
#             if key == "d":
#                 #Delete
#                 break
#             elif key == "s":
#                 rospy.spin()
#                 break

