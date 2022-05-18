from rtde_receive import RTDEReceiveInterface as RTDEReceive
import time
import sys

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

