#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class setup:

    def __init__(self):
        self.pub = rospy.Publisher('NrOfRois', String, queue_size=self.nrOfRois)
        rospy.init_node('setup', anonymous=True)
        rate = rospy.Rate(10) #10Hz
        
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            rate.sleep()

    def callback(self):
        bridge = CvBridge()
        rospy.loginfo(rospy.get_caller_id() + "Camera Image recieved")
        try:
            self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)
    
    def publish_data(self):
        return 0

def main():
    m = setup(10)
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
