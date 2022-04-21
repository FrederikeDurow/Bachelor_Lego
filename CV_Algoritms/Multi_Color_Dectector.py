import numpy as np
import cv2
import time
import csv

from random import randint #random numbers

# THREE DIFFERENT COLOR DETECTOR
#output  =cv2.VideoWriter("Multicolor.avi", cv2.VideoWriter_fourcc(*'MPEG'), 30 , (1456,1088))

class multi_color_dectector():

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
    
    def __init__(self,rois):
        self.red = (0, 0, 255)
        self.green = (0, 255, 0)
        self.blue  = (255, 0, 0)

        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0

        self.create_data_file(rois)

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

        self.countours_red, self.hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.countours_green, self.hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        self.countours_blue, self.hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0

        for c in self.countours_blue:
            x,y,w,h = cv2.boundingRect(c)
            if w*h > self.w_large*self.h_large:
              self.w_large = w
              self.h_large = h
              self.x_large = x
              self.y_large = y
        self.add_data()

    def add_data(self):
        self.data_blue.append('')
        self.data_blue.append(self.x_large)
        self.data_blue.append(self.y_large)
        self.data_blue.append((self.w_large/2)+self.x_large)
        self.data_blue.append((self.h_large/2)+self.y_large)

    def drawRegions(self, color_pick, area_size):
        if color_pick.upper() == 'BLUE':
            color = self.blue
            countours = self.countours_blue
        elif color_pick.upper() == 'GREEN':
            color = self.green
            countours = self.countours_green
        elif color_pick.upper() == 'RED':
            color = self.red
            countours = self.countours_red
        else:
            print('Input dont match an implemented color')

        for pic, contour in enumerate(countours):
            area = cv2.contourArea(contour)
            if(area > area_size):
                x, y, w, h = cv2.boundingRect(contour)
                self.output_img = cv2.rectangle(self.frame, (x, y), (x + w, y + h), color, 2)
        return self.output_img

    def dataOutput(self):
        return self.data_blue

    def create_data_file(self,rois):
        print()
        header = ['Lap Nr']
        roi = 0
        while True:
            if roi < rois:
                header.append('Roi'+str(roi+1))
                header.append('Roi'+str(roi+1)+'_x')
                header.append('Roi'+str(roi+1)+'_y')
                header.append('Roi'+str(roi+1)+'_center_x')
                header.append('Roi'+str(roi+1)+'_center_y')
                roi += 1
            else:
                break

        with open('MultiColorTracker_Data.csv', 'w', encoding='UTF8', newline='') as f:      ############################3333
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
            f.close()

    def save_data(self, frame_nr):
        self.data_blue.insert(0, frame_nr)
        with open("MultiColorTracker_Data.csv", 'a', encoding='UTF8', newline='') as f:      ################################
            writer = csv.writer(f)
            # write data row
            writer.writerow(self.data_blue)
            self.data_blue.clear()
            f.close()
    

# ---- HOW TO USE -----
videofeed = cv2.VideoCapture("/home/rasmus/Desktop/Test Videos/Test/07-04/Big Springs/100-Correct-Laps.mp4")
time.sleep(2.0)

#header = ['Lap Nr', 'Point 1', 'X', 'Y','w/2','h/2']
#with open('Multicolor_data.csv', 'w', encoding='UTF8', newline='') as f:      ############################3333
#    writer = csv.writer(f)
#    # write the header
#    writer.writerow(header)
#    f.close()
#
frame_counter = 0

rois = []
colors = []

ret, init_frame = videofeed.read()

while True:
    roi = cv2.selectROI('Multi Tracker', init_frame)
    rois.append(roi)
    colors.append((randint(0, 255), randint(0,255), randint(0,255)))

    print('Press S to start tracking')
    print('Press any other key to select the next object')

    k = cv2.waitKey(0) & 0XFF
    if k == 115: 
      MultiColor = multi_color_dectector(len(rois))
      break

while True:
    _, imageFrame = videofeed.read()
    frame_counter +=1

    for roi in rois:
        crop_img = imageFrame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]

        MultiColor.applyColorDectector(crop_img)
        Multi_img = MultiColor.drawRegions('BLUE', 100) 

        imageFrame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]] = Multi_img
        MultiColor.save_data(frame_counter)

    #output.write(frame) 
    cv2.imshow("Multiple Color Detector", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
