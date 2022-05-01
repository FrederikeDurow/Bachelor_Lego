#!/usr/bin/env python3
import rospy
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class data_editor:

    def __init__(self):
        self.sub = rospy.Subscriber("LapOutcome", String, self.callback)
       
    def callback(self, data):
        print("hello")
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

def main():
    rospy.init_node('data_editor', anonymous=True)
    de = data_editor()
    rospy.spin()

if __name__ == '__main__':
    main()