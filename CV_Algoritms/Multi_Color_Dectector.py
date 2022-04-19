import numpy as np
import cv2
import time

# THREE DIFFERENT COLOR DETECTOR

class multi_color_dectector():

    frame = None

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

    def applyColorDectector(self, frame):
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

        self.contours, self.hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.drawRegions(self.red, 100)

        self.contours, self.hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.drawRegions(self.green, 100)

        self.contours, self.hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.drawRegions(self.blue, 100)

        return self.frame, self.contours

    def drawRegions(self, color, area_size):
        for pic, contour in enumerate(self.contours):
            area = cv2.contourArea(contour)
            if(area > area_size):
                x, y, w, h = cv2.boundingRect(contour)
                self.frame = cv2.rectangle(self.frame, (x, y), (x + w, y + h), color, 2)

# ---- HOW TO USE -----

Dectector = multi_color_dectector()

videofeed = cv2.VideoCapture(0)
time.sleep(2.0)

while(1):
    _, imageFrame = videofeed.read()

    cv2.imshow("Multiple Color Detector", Dectector.applyColorDectector(imageFrame))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
