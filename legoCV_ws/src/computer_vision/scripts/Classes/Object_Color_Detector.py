import cv2
from cv2 import boundingRect
import numpy as np


class obj_color_dectector():
    
    frame = None
    output_img = None

    countours = None 
    data = []
    # countours_red = None
    # countours_green = None
    # countours_blue = None

    # data_red = []
    # data_green = []
    # data_blue = []

    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)

    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)

    #ADD MORE LOWER/UPPER FOR MORE COLORS
    
    def __init__(self):
        pass
        # self.red = (0, 0, 255)
        # self.green = (0, 255, 0)
        # self.blue  = (255, 0, 0)

    def applyColorDectector(self, frame,color, size):                                             #We need to hardcode size
        self.color = color
        self.data.clear()
        self.frame = frame
        hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        if self.color == "r":
            mask = cv2.inRange(hsvFrame, self.red_lower, self.red_upper)
        elif self.color == "g":
            mask = cv2.inRange(hsvFrame, self.green_lower, self.green_upper)
        else:
            mask = cv2.inRange(hsvFrame, self.blue_lower, self.blue_upper)

        
        # Morphological Transform, Dilation
        # for each color and bitwise_and operator
        # between imageFrame and mask determines
        # to detect only that particular color
        kernel = np.ones((5, 5), "uint8")

        mask = cv2.dilate(mask, kernel)
        #res= cv2.bitwise_and(self.frame, self.frame, mask)

        self.countours, self.hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        for c in self.countours:
            x,y,w,h = cv2.boundingRect(c)
            area = (w)*(h)
            bounding = [x,y,w,h,area]
            if area > size:
                self.data.append(bounding)
        return self.data


# self.frame = frame
#         if self.color == "r":
#             self.redDetector()
#         elif self.color == "g":
#             self.greenDetector()
#         else:
#             self.blueDetector()