from matplotlib.style import available
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from os.path import exists
import time
import argparse
import sys
import cv2



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
        default='192.168.1.68',
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
        "-f",
        "--frequency",
        dest="frequency",
        help="the frequency at which the data is recorded (default is 500Hz)",
        type=float,
        default=500.0,
        metavar="<frequency>")

    return parser.parse_args(args)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    data_to_record =['timestamp', 'actual_TCP_pose']
    dt = 1 / args.frequency
    rtde_r = RTDEReceive(args.ip, args.frequency)
    rtde_r.startFileRecording(args.output, data_to_record)
    print("Data recording started, press [Ctrl-C] to end recording.")
    i = 0
    try:
        while True:
            start = time.time()
            # if i % 10 == 0:
            #     sys.stdout.write("\r")
            #     sys.stdout.write("{:3d} samples.".format(i))
            #     sys.stdout.flush()
            end = time.time()
            duration = end - start

            if duration < dt:
                time.sleep(dt - duration)
            i += 1

    except KeyboardInterrupt:
        rtde_r.stopFileRecording()
        print("\n[MSG] Data recording stopped.")


if __name__ == "__main__":
    main(sys.argv[1:])










def record_data(counter, frequency):
    #args = parse_args(args)
    dt = 1 / frequency
    start = time.time()
    if counter % 10 == 0:
        sys.stdout.write("\r")
        sys.stdout.write("{:3d} samples.".format(counter))
        sys.stdout.flush()
    end = time.time()
    duration = end - start
    if duration < dt:
        time.sleep(dt - duration)
    counter += 1
    return counter

#def data_to_output():
#
#    available_data = ['timestamp','actual_TCP_pose','actual_TCP_force']
#    data_output = []
#
#    print("[INFO] See the guide from Vister for the enabling of wanted data \n")
#    time.sleep(2.0)
#    print("[INFO] Select the .txt with the data to be stored in it \n")
#    while True:
#        file = input('[WAIT USER] Enter the full path to the data output settings: ')
#        if exists(file):
#            data_to_be_stored = open(file, encoding='utf-8').read()
#            break
#        else:
#            print("[MSG] Could not find file")
#            time.sleep(2.0)
#    
#    print("[MSG] Data setting file was succesfully read!")
#    data_output.append(data_to_be_stored)
#    print(data_output)
#    k = input('[WAIT USER] Enter the whished name for the CSV file: ')
#    csv_file = str(k)+".csv"
#
#    return data_output, csv_file

def data_to_output():
    
    available_data = ['timestamp','actual_execution_time','actual_TCP_pose','actual_TCP_speed','actual_TCP_force','runtime_state']
    data_output = []

    #print("[INFO] See the guide from Vister for the enabling of wanted data \n")
    print("\n[INFO] Data that can be stored: " + str(available_data))
    while True:
        file = str(input('\n[WAIT USER] Enter 1 to enable and 0 to uenable recording of data \n(e.g. 100 to only record timestamp): '))
        if len(file) == len(available_data):
            data_to_be_stored = file
            break
        else:
            print("\n[MSG] The input doesn't match the requriement or size of available_data")

    checker = 0
    for i in available_data:
        if data_to_be_stored[checker] == '1':
            data_output.append(available_data[checker])
        checker +=1
    
    #print("[MSG] Data to be saved was succesfully set!\n")
    #data_output.append(data_to_be_stored)
    #print(data_output)
    k = input('\n[WAIT USER] Enter the whished name for the CSV file: ')
    csv_file = str(k)+".csv"

    return data_output, csv_file
