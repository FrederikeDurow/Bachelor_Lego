# import Ours.UR_Csv_Writer as UR_csv_writer
import sys,os
import rospy
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
# sys.path.insert(0, '/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/legoCV_ws/src/computer_vision/scripts')
from Vister_Classes import URControl

def main():
    rospy.init_node('UR-Robot', anonymous=True)
    ur = URControl.ur_robot()
    rospy.spin()
    
if __name__ == '__main__':
    main()