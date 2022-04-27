# import Ours.UR_Csv_Writer as UR_csv_writer
import sys
sys.path.insert(0, '/home/rasmus/Bachelor/Bachelor_Lego/UR')
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from Ours import PlayURPWorks as PURP
from Ours import RecordDataWorks as record
import time

#IP = '192.168.1.68'
#PORT = 30004
#IP = input("Enter IP of Robot:")
#PORT = 30004

robot_dash, ip = PURP.establish_connection()
PURP.check_robot_mode(robot_dash)
PURP.loadURscript(robot_dash,'1234')

data_to_record, output_file = record.data_to_output()
frequency = float(input("[WAIT USER] insert frequency of data saving (default = 500): "))
robot_recive = RTDEReceive(ip,frequency)

datatest = ['timestamp']

print("\n[MSG] Waiting for start running signal\n")
time.sleep(2.0)

input("[WAIT USER] Enter any key to start: ")

while True:
    robot_recive.startFileRecording(output_file, datatest)
    counter = 0

    while robot_dash.isConnected() == True:
        record.record_data(counter, frequency)
        
    robot_recive.stopFileRecording()

#       
#       robot_dash.play()
#       while
#       while robot_dash.isRunning() == True:
#           pass
#   
