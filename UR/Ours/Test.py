import sys
sys.path.append('/home/rasmus/Bachelor/Bachelor_Lego/UR')
import logging

import rtde.rtde as rtde
import rtde.rtde_config as rtde_config

ROBOT_HOST = '192.168.1.68'
ROBOT_PORT = 30004

con = rtde.RTDE(ROBOT_HOST, ROBOT_PORT)
con.connect()
if con.is_connected():
    print('halleluja!')

con.send_start()

# get controller version
con.get_controller_version()