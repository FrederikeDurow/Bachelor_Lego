import cv2
from cv2 import boundingRect
import numpy as np
import time

class obj_color_dectector():
    
    frame = None
    output_img = None

    countours_red = None
    countours_green = None
    countours_blue = None

    data_red = []
    data_green = []
    data_blue = []

    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)

    #ADD MORE LOWER/UPPER FOR MORE COLORS
    
    def __init__(self):
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.blue  = (255, 0, 0)

    def applyColorDectector(self, frame, size):                                             #We need to hardcode size
        self.data_blue.clear()
        self.frame = frame
        hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        red_mask = cv2.inRange(hsvFrame, self.red_lower, self.red_upper)
        green_mask = cv2.inRange(hsvFrame, self.green_lower, self.green_upper)
        blue_mask = cv2.inRange(hsvFrame, self.blue_lower, self.blue_upper)

        # Morphological Transform, Dilation
        # for each color and bitwise_and operator
        # between imageFrame and mask determines
        # to detect only that particular color
        kernal = np.ones((5, 5), "uint8")

        # For red color
        red_mask = cv2.dilate(red_mask, kernal)
        res_red = cv2.bitwise_and(self.frame, self.frame, mask = red_mask)

        # For green color
        green_mask = cv2.dilate(green_mask, kernal)
        res_green = cv2.bitwise_and(self.frame, self.frame, mask = green_mask)

        # For blue color
        blue_mask = cv2.dilate(blue_mask, kernal)
        res_blue = cv2.bitwise_and(self.frame, self.frame, mask = blue_mask)

        self.countours_red, self.hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.countours_green, self.hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.countours_blue, self.hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in self.countours_blue:
            x,y,w,h = cv2.boundingRect(c)
            area = (w)*(h)
            bounding_blue = [x,y,w,h,area]
            if area > size:
                self.data_blue.append(bounding_blue)
        return self.data_blue
