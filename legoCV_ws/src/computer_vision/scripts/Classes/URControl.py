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
                    self.robot_dash.play()
                    time.sleep(2.0)
                else:
                    self.counter = record.record_data(self.counter, self.frequency)
                   
            self.robot_dash.pause()
            #print("\n[MSG] Waiting for start running signal\n")
            return True

    def test_done(self):
        self.robot_dash.stop()
        self.robot_dash.disconnect()
        self.robot_recive.stopFileRecording()
        return True