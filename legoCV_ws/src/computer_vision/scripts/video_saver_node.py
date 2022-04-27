#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class video_saver:

    def __init__(self):
        self.cvimg = None
        self.sub = rospy.Subscriber("/pylon_camera_node/image_raw", Image, self.callback)
        fourcc = cv2.VideoWriter_fourcc(*'MP4V')
        self.out = cv2.VideoWriter('ny.mp4', fourcc, 100.0, (1440,1080), 0)

    def callback(self, data):
        bridge = CvBridge()
        rospy.loginfo(rospy.get_caller_id() + "Camera Image recieved")
        try:
            self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)
            
        self.cv_show()
        self.save_video()

    def cv_show(self):
        cv2.imshow("cv image", self.cvimg)
        cv2.waitKey(10)

    def save_video(self): 
        self.out.write(self.cvimg)    
    
    def stream_closed(self):
        self.out.release()

        
def main():
    rospy.init_node('stream', anonymous=True)
    sub = video_saver()
    rospy.spin()
    sub.stream_closed()
    
if __name__ == '__main__':
    main()

