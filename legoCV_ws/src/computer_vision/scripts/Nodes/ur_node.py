# import Ours.UR_Csv_Writer as UR_csv_writer
import sys
import rospy
sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Classes import URControl

def main():
    rospy.init_node('UR-Robot', anonymous=True)
    ur = URControl.ur_robot()
    rospy.spin()
    
if __name__ == '__main__':
    main()