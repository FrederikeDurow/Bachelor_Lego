#!/usr/bin/env python3
from cv2 import imread
import rospy
import cv2
import os
import glob
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class MalfunctionVideoSaver:
    testStatus = "Waiting"
    image_counter = 0
    cvimg = None

    def __init__(self, path):
        self.path = path
        self.vidName = None
        
        #Create subscriber to Camera
        self.camSub = rospy.Subscriber("/pylon_camera_node/image_rect", Image, self.camCallback)

    def camCallback(self, data):
        #print(self.testStatus)
        bridge = CvBridge()
        try:
            self.cvimg = bridge.imgmsg_to_cv2(data, desired_encoding='passthrough')       
        except CvBridgeError as e:
            print(e)

        if self.testStatus == "Running":
            #print("realizing it is running")
            self.add_to_video()   
        else:
            pass

    def cv_show(self):
        cv2.imshow("Mal image", self.cvimg)
        cv2.waitKey(10)
    
    def start_recording(self,name):
        print("Starting again")
        self.vidName = name+'.avi'
        self.testStatus = "Running"
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        self.out = cv2.VideoWriter(os.path.join(self.path,self.vidName), fourcc, 12, (1440,1080), 1)
        
    def add_to_video(self): 
        print("Adding image")
        self.out.write(self.cvimg) 

    def stop_recording(self):
        print("Releasing Video")
        self.testStatus = "Stop"
        #print("In stop_recording")
        self.out.release()

       
    
    def delete_video(self):
        #self.out.delete()
        print("Deleting Video")
        try:
            os.remove(os.path.join(self.path,self.vidName))
        except:
            pass
        
    # def save_video(self):
    #     self.testStatus = "Waiting"
    #     self.out.release()

    # def update_buffer(self, new_img):
    # #Save newest camera stream frame
    #     fileName = str(self.image_counter)+".jpg"
    #     cv2.imwrite(os.path.join(self.path, fileName), new_img)
    #     self.image_counter += 1

    # def reset_buffer(self):
    # #Delete all saved images
    #     for i in range(self.image_counter):
    #         fileName = str(i)+".jpg"
    #         os.remove(os.path.join(self.path,fileName))

    # def cv_show(self):
    #     cv2.imshow("cv image", self.cvimg)
    #     cv2.waitKey(10)
    
    # def start_recording(self):
    #     self.testStatus = "Running"
    
    # def stop_recording(self):
    #     self.testStatus = "Done"

    # def save_video(self, name): 
    # #Make video out of buffer images
    #     fourcc = cv2.VideoWriter_fourcc(*'MPEG')
    #     self.out = cv2.VideoWriter(name+'.avi', fourcc, 24, (1440,1080), 1)
    #     for imageName in glob.glob(os.path.join(self.path,"*.jpg")):
    #         next_image = cv2.imread(imageName)
    #         self.out.write(next_image)   
    #     self.out.release() 

