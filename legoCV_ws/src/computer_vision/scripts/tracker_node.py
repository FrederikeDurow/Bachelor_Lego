#!/usr/bin/env python3
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class matcher:

    def __init__(self, objects):
        self.nrOfOs = objects
        self.pub = rospy.Publisher('LapOutcome', String, queue_size=self.nrOfOs)
        rospy.init_node('Matcher', anonymous=True)
        rate = rospy.Rate(10) #10Hz
        
        while not rospy.is_shutdown():
            hello_str = "hello world %s" % rospy.get_time()
            rospy.loginfo(hello_str)
            self.pub.publish(hello_str)
            rate.sleep()

    def callback(self):
        print("hello")
        
def main():
    m = matcher(10)
    
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass