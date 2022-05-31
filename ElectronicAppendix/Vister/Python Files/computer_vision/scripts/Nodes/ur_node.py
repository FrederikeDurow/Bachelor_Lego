# import Ours.UR_Csv_Writer as UR_csv_writer
import os
import sys

import rospy

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(os.path.dirname(dir_path),'Nodes'))
from Vister_Classes import URControl


def main():
    rospy.init_node('UR-Robot', anonymous=True)
    URControl.ur_robot()
    rospy.spin()
    
if __name__ == '__main__':
    main()
