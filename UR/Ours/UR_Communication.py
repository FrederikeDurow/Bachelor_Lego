from distutils.command.config import config
import sys

from UR.examples.example_control_loop import ROBOT_PORT
sys.path.append('..')
import logging

import UR.Ours.UR_Utilities as UR_Utilities
import rtde.rtde_config as rtde_config


def Robot_Host_set (input):
    ROBOT_HOST = input

def Robot_Port_set (input):
    ROBOT_PORT = input

def Config_file_set(str):
    config_filename = str

def Load_URP_script(str):
    if(str.endswith('.urp')):
        URP_script = str
    else:
        print('Wrong file type. Please load an .urp file')


