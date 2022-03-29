import rtde_control
import rtde_receive
import rtde_io
import time
import argparse
import dashboard_client
from pynput.keyboard import Key, Controller

# Note: In order to make this work, make sure that there is
# not any custom set URcap IP/port. Additinally, have at least 2
# move node, as it will only move between waypoint if is set up like that


ROBOT_IP = '192.168.1.68'
ROBOT_PORT = 30004

rtde_c = rtde_control.RTDEControlInterface(ROBOT_IP)
rtde_io1 =rtde_io.RTDEIOInterface(ROBOT_IP)
rtde_das =dashboard_client.DashboardClient(ROBOT_IP)

keyboard = Controller()

rtde_das.connect()
if rtde_das.isConnected():
    print('Connection to Dashboard is live')

#rtde_das.powerOn()
#rtde_das.brakeRelease()
rtde_das.loadURP('1234.urp')
rtde_das.play()

#while True:
#    if keyboard.press('p'):
#        rtde_das.pause()
#        print("Pausing")
#    if keyboard.press('q'):
#        rtde_das.stop()
#        print("Stoping")
#        break






#rtde_r = rtde_receive.RTDEReciveInterface(ROBOT_IP,ROBOT_PORT)

#actual_TCP_pose = rtde_r.getActualTCPpose()
#actual_TCP_force = rtde_r.getActualTCPForce()

#actual_TCP_speed = rtde_r.getActualTCPSpeed()  



#class StatusSwitcher:
 #   def swichter(self,scenario):
  #      default = "Error"
#
 #       return getattr(self,'case_'+str(scenario), lambda:default)()

def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Record data example")
    parser.add_argument(
        "-ip",
        "--robot_ip",
        dest="ip",
        help="IP address of the UR robot",
        type=str,
        default='localhost',
        metavar="<IP address of the UR robot>")
    parser.add_argument(
        "-o",
        "--output",
        dest="output",
        help="data output (.csv) file to write to (default is \"robot_data.csv\"",
        type=str,
        default="robot_data.csv",
        metavar="<data output file>")
    parser.add_argument(
        "-t",
        "--Time_stamp",
        dest="Time Stamp",
        help="Time elapsed since the controller was started [s]",
        type=Double,
        default=0,
        metavar="<Time_stamp>")
    parser.add_argument(
        "-f",
        "--frequency",
        dest="frequency",
        help="the frequency at which the data is recorded (default is 500Hz)",
        type=float,
        default=500.0,
        metavar="<frequency>")
    parser.add_argument(
        "-TCP_P",
        "--TCPpose",
        dest="actual_TCP_pose",
        help="the actual TCP pose at a given point",
        type=float,
        default=0,
        metavar="<actual_TCP_pose>")
    parser.add_argument(
        "-TCP_F",
        "--TCPforce",
        dest="actual_TCP_force",
        help="the actual TCP force at a given point",
        type=float,
        default=0,
        metavar="<actual_TCP_force>")
    parser.add_argument(
        "-TCP_S",
        "--TCPspeed",
        dest="actual_TCP_force",
        help="the actual TCP speed at a given point",
        type=float,
        default=0,
        metavar="<actual_TCP_speed>")

    return parser.parse_args(args)