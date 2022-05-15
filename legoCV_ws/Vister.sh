#!/bin/env bash
source /opt/ros/noetic/setup.bash
source /home/rasmus/Bachelor/Bachelor_Lego/legoCV_ws/setup.bash


gnome-terminal -x sh -c “roscore|less”
gnome-terminal -x sh -c “roslaunch pylon_camera pylon_camera_node|less”
gnome-terminal -x sh -c “roslaunch computer_vision computer_vision_start.launch|less”

