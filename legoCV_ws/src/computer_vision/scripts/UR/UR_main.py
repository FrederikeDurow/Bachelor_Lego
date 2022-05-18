# import Ours.UR_Csv_Writer as UR_csv_writer
import sys
sys.path.insert(0, '/home/rasmus/Bachelor/Bachelor_Lego/UR')
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import rtde_io
import UR_connection as UR_con
import UR_record as UR_rec
import time

#IP = '192.168.1.68'
#PORT = 30004
#IP = input("Enter IP of Robot:")
#PORT = 30004

robot_dash, ip = UR_con.establish_connection()
UR_con.check_robot_mode(robot_dash)
UR_con.loadURscript(robot_dash)

data_to_record, output_file = UR_rec.data_to_output()
frequency = float(input("[WAIT USER] insert frequency of data saving (default = 500): "))
robot_recive = RTDEReceive(ip,frequency)
rtde_in_out =rtde_io.RTDEIOInterface(ip)

#datatest = ['timestamp']

print("\n[MSG] Waiting for start running signal\n")
time.sleep(2.0)

input("[WAIT USER] Enter any key to start: ")
rtde_in_out.setStandardDigitalOut(0,True)
rtde_in_out.setStandardDigitalOut(1,False)
rtde_in_out.setStandardDigitalOut(2,False)
rtde_in_out.setStandardDigitalOut(3,False)
rtde_in_out.setStandardDigitalOut(4,False)
rtde_in_out.setStandardDigitalOut(5,False)
rtde_in_out.setStandardDigitalOut(6,False)
rtde_in_out.setStandardDigitalOut(7,False)

while True:
    robot_recive.startFileRecording(output_file, data_to_record)
    counter = 0
    Computer_vison_flag = 0

    while robot_dash.isConnected() == True:
        UR_rec.record_data(counter, frequency)
        
        # Sets all digital outputs low
        # --- A CALL FROM COMPUTER VISION SITE TO CALL THE FOLLOWING (SUDO)
        # if ros signal == activated():
            # for i robot_recive.getActualDigitalOutputBits():
                #robot_recive.setStandardDigitalOut(i,False)
        
        print("ADOB: " +str(robot_recive.getActualDigitalOutputBits()))

        while robot_recive.getActualDigitalOutputBits() != False:
            print("Computer Vision is prossesing")
            time.sleep(4.0)
            rtde_in_out.setStandardDigitalOut(0,False)
            rtde_in_out.setStandardDigitalOut(1,False)
            rtde_in_out.setStandardDigitalOut(2,False)
            rtde_in_out.setStandardDigitalOut(3,False)
            rtde_in_out.setStandardDigitalOut(4,False)
            rtde_in_out.setStandardDigitalOut(5,False)
            rtde_in_out.setStandardDigitalOut(6,False)
            rtde_in_out.setStandardDigitalOut(7,False)
            time.sleep(1.0)
    
        while robot_recive.getActualDigitalOutputBits() == False:    
            if robot_dash.running() == False:
                print("Starting Loop")
                robot_dash.play()
                time.sleep(2.0)
            else:
                pass
            # ---- THE SCRIPT WILL SET ONE OF THE DIGITALOUTPUTBITS HIGH ----
        
        # Makes sure to stop the UR until the Computer Vision has taken place
        print("End of loop")
        if robot_dash.running() == True:
            robot_dash.pause()
            # --- A CALL FROM UR SITE TO CALL COMPUTER VISION
        else:
            pass

    robot_recive.stopFileRecording()

    print("\n[MSG] Waiting for start running signal\n")


#
#while True:
#    robot_recive.startFileRecording(output_file, datatest)
#    counter = 0
#    Computer_vison_flag = 0
#
#    while robot_dash.isConnected() == True:
#        record.record_data(counter, frequency)
#        
#        # Sets all digital outputs low
#        # --- A CALL FROM COMPUTER VISION SITE TO CALL THE FOLLOWING (SUDO)
#        # if ros signal == activated():
#            # for i robot_recive.getActualDigitalOutputBits():
#                #robot_recive.setStandardDigitalOut(i,False)
#
#        while True in robot_recive.getActualDigitalOutputBits():
#            print("Computer Vision is prossesing")
#            time.sleep(4.0)
#            for i in robot_recive.getActualDigitalOutputBits():
#                robot_recive.setStandardDigitalOut(i,False)
#    
#        while True not in robot_recive.getActualDigitalOutputBits():    
#            if robot_dash.isRunning() == False:
#                robot_dash.play()
#            else:
#                pass
#            # ---- THE SCRIPT WILL SET ONE OF THE DIGITALOUTPUTBITS HIGH ----
#        
#        # Makes sure to stop the UR until the Computer Vision has taken place
#        print("End of loop")
#        if robot_dash.isRunning() == True:
#            robot_dash.pause()
#            # --- A CALL FROM UR SITE TO CALL COMPUTER VISION
#        else:
#            pass
#
#    robot_recive.stopFileRecording()
#
#    print("\n[MSG] Waiting for start running signal\n")
#
##       
#       robot_dash.play()
#       while
#       while robot_dash.isRunning() == True:
#           pass
#   
