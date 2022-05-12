import rtde_control
import rtde_receive
import rtde_io
import time
import dashboard_client

# Note: In order to make this work, make sure that there is
# not any custom set URcap IP/port. Additinally, have at least 2
# move node, as it will only move between waypoint if is set up like that

def establish_connection():
    IP = '192.168.1.68'
    ROBOT_IP = IP
    #ROBOT_IP = input("Enter IP-address of Robot: ")
    robot_dash =dashboard_client.DashboardClient(ROBOT_IP)

    while robot_dash.isConnected() != True:
            robot_dash =dashboard_client.DashboardClient(ROBOT_IP)
            try:
                robot_dash.connect()
            finally:
                if robot_dash.isConnected() != True:
                    print("[MSG] Failed to connect with the given IP-address")
                    print("[MSG] Please check connect and the entered IP-address")
                    ROBOT_IP = input("[WAIT USER] Enter IP-address of Robot: ")

    if robot_dash.isConnected():
        print('\n[INFO] Program is now connected to:')
        print('[INFO] Robot Model:' + str(robot_dash.getRobotModel()))
        print('[INFO] Serial Number:' + str(robot_dash.getSerialNumber()))
        print('\n[MSG] Connection to Dashboard is live!')

    return robot_dash, IP


def check_robot_mode(connected_UR):

    robot_dash = connected_UR

    if robot_dash.isInRemoteControl() != True:
        print('[MSG] Make sure the '+str(robot_dash.getRobotModel())+" is in Remote Control")

    while robot_dash.isInRemoteControl() != True:
        pass

    if robot_dash.isInRemoteControl() == True:
        robot_dash.connect() # It has to connect again to establish the connection in Remote Control
        print('\n[MSG] Powering on')
        robot_dash.powerOn()
        time.sleep(4.0)
        print('\n[MSG] Releasing brakes')
        robot_dash.brakeRelease()
        time.sleep(4.0)
        print("\n[MSG] Robot is ready for operation \n")

    return robot_dash

def loadURscript (connected_UR):
    urp_file = str(input("[WAIT USER] Enter the name of the .urp script file: "))
    robot_dash = connected_UR
    script_file = str(urp_file)+'.urp' 

    robot_dash.loadURP(script_file)
    print("[INFO] " + str(robot_dash.getLoadedProgram()))

    return robot_dash
