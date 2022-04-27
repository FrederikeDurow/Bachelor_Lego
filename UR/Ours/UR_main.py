# import Ours.UR_Csv_Writer as UR_csv_writer
import sys
sys.path.insert(0, '/home/rasmus/Bachelor/Bachelor_Lego/UR')
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import rtde_io
from Ours import PlayURPWorks as PURP
from Ours import RecordDataWorks as record
import time

#IP = '192.168.1.68'
#PORT = 30004
#IP = input("Enter IP of Robot:")
#PORT = 30004

robot_dash, ip = PURP.establish_connection()
PURP.check_robot_mode(robot_dash)
urp_file = str(input("[WAIT USER] Enter the name of the .urp script file "))
PURP.loadURscript(robot_dash)

data_to_record, output_file = record.data_to_output()
frequency = float(input("[WAIT USER] insert frequency of data saving (default = 500): "))
robot_recive = RTDEReceive(ip,frequency)
rtde_in_out =rtde_io.RTDEIOInterface(ip)

datatest = ['timestamp']

print("\n[MSG] Waiting for start running signal\n")
time.sleep(2.0)

input("[WAIT USER] Enter any key to start: ")

while True:
    robot_recive.startFileRecording(output_file, datatest)
    counter = 0

    while robot_dash.isConnected() == True:
        record.record_data(counter, frequency)
        
        # Sets all digital outputs low
        # --- A CALL FROM COMPUTER VISION SITE TO CALL THE FOLLOWING (SUDO)
        # if ros signal == activated():
            # for i robot_recive.getActualDigitalOutputBits():
                #robot_recive.setStandardDigitalOut(i,False)
        # while robot_recive.getActualDigitalOutputBits() = [False, False, False, False, False, False, False]
        while True not in robot_recive.getActualDigitalOutputBits():
            if robot_dash.isRunning() == False:
                robot_dash.play()
            else:
                pass
            # ---- THE SCRIPT WILL SET ONE OF THE DIGITALOUTPUTBITS HIGH ----
        
        # Makes sure to stop the UR until the Computer Vision has taken place
        if robot_dash.isRunning() == True:
            robot_dash.pause()
            # --- A CALL FROM UR SITE TO CALL COMPUTER VISION
        else:
            pass

    robot_recive.stopFileRecording()

    print("\n[MSG] Waiting for start running signal\n")

#       
#       robot_dash.play()
#       while
#       while robot_dash.isRunning() == True:
#           pass
#   
