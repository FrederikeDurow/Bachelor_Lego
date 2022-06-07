#!/usr/bin/env python3
#!/bin/bash
import os
import time
import rospy
import roslaunch 
import subprocess
roscore = subprocess.Popen('roscore')
time.sleep(1)

#os.system("roslaunch pylon_camera pylon_camera_node.launch")
#time.sleep(4.0)
#os.system("roslaunch computer_vision computer_vision_start.launch")
dir_path = os.path.dirname(os.path.realpath(__file__))

rospy.init_node('en_Mapping', anonymous=True)
uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
roslaunch.configure_logging(uuid)

# STARTING UP CAMERA
launch = roslaunch.parent.ROSLaunchParent(uuid, [str(dir_path) +"/src/pylon-ros-camera/pylon_camera/launch/pylon_camera_node.launch"])
launch.start()


time.sleep(5.0)

# STARTING UP VISTER
launch2 = roslaunch.parent.ROSLaunchParent(uuid, [str(dir_path) +"/src/computer_vision/launch/computer_vision_start.launch"])
launch2.start()

exec /bin/bash
rospy.spin()
