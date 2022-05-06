# import Ours.UR_Csv_Writer as UR_csv_writer
import sys
import rospy
from computer_vision.srv import Robo, RoboResponse
from std_msgs.msg import Bool
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from rtde_receive import RTDEReceiveInterface as RTDEReceive
import rtde_io
from UR.Ours import PlayURPWorks as PURP
from UR.Ours import RecordDataWorks as record
import time

class ur_robot:
    def __init__(self):
        #Wait for start signal from Setup_Node
        self.start = False
        self.sub = rospy.Subscriber("StartRobot", Bool, self.startCallback)

        while self.start == False:
            pass
            
        self.counter = 0
        self.robot_dash, self.ip = PURP.establish_connection()
        PURP.check_robot_mode(self.robot_dash)
        PURP.loadURscript(self.robot_dash)

        self.data_to_record, self.output_file = record.data_to_output()
        self.frequency = float(input("[WAIT USER] Insert frequency of data saving (default = 500): "))
        self.robot_recive = RTDEReceive(self.ip,self.frequency)
        self.rtde_in_out =rtde_io.RTDEIOInterface(self.ip)

        self.robot_recive.startFileRecording(self.output_file, self.data_to_record)
        #self.record()
        self.roboSrv = rospy.Service("RunNextLap", Robo, self.callback)
    
    def startCallback(self, data):
        self.start = data

    def record(self):
        while self.robot_dash.isConnected() == True:
                self.counter = record.record_data(self.counter, self.frequency)                         #SKAL ÆNDRES, så den direkte bruger self.counter 

    def callback(self, request):
        if request.start == True:
            return RoboResponse(self.run_lap())
        elif request.start == False:
            return RoboResponse(self.test_done())
        #return RoboResponse(True)
      

    def run_lap(self):

        #print("\n[MSG] Start running\n")

        self.rtde_in_out.setStandardDigitalOut(0,False)
        self.rtde_in_out.setStandardDigitalOut(1,False)
        self.rtde_in_out.setStandardDigitalOut(2,False)
        self.rtde_in_out.setStandardDigitalOut(3,False)
        self.rtde_in_out.setStandardDigitalOut(4,False)
        self.rtde_in_out.setStandardDigitalOut(5,False)
        self.rtde_in_out.setStandardDigitalOut(6,False)
        self.rtde_in_out.setStandardDigitalOut(7,False)

        if self.robot_dash.isConnected() == True:
            while self.robot_recive.getActualDigitalOutputBits() == False:    
                if self.robot_dash.running() == False:
                    #print("\n[MSG] Starting Loop\n")
                    self.robot_dash.play()
                    time.sleep(2.0)
                else:
                    self.counter = record.record_data(self.counter, self.frequency)
                   
    
         
                # ---- THE SCRIPT WILL SET ONE OF THE DIGITALOUTPUTBITS HIGH ----
            
            # Makes sure to stop the UR until the Computer Vision has taken place
            #print("\n[MSG] End of loop\n")
            self.robot_dash.pause()
            print("\n[MSG] Waiting for start running signal\n")
            return True

    def test_done(self):
        self.robot_dash.stop()
        self.robot_dash.disconnect()
        self.robot_recive.stopFileRecording()
        return True

def main():
    rospy.init_node('UR-Robot', anonymous=True)
    ur = ur_robot()
    #ur.setup
    rospy.spin()
    
if __name__ == '__main__':
    main()

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