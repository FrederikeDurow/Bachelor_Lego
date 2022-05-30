import numpy as np
import cv2
import csv

class BoundingBox():
    
    img = None
    countours = None

    output_img = None

    def __init__(self, rois):
        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0
        self.data = []
        #self.create_data_file(rois)

    def applyBoundingBox(self,image):
        self.img = image
        self.original = image
        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("/home/frederike/Desktop/gray.png", gray_img)
        thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        cv2.imwrite("/home/frederike/Desktop/thresh.png", thresh_img)

        self.contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
        #c_img = image
        #cv2.drawContours(c_img, self.contours, -1, (0,255,0), 2, cv2.LINE_AA)
        #cv2.imwrite("/home/frederike/Desktop/contours.png", c_img)

        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0

        # find largest bounding box
        for c in self.contours:
            x,y,w,h = cv2.boundingRect(c)
            if w*h > self.w_large*self.h_large:
              self.w_large = w
              self.h_large = h
              self.x_large = x
              self.y_large = y
        self.add_data()
    
    def add_data(self):
        self.data.append('')
        self.data.append(self.x_large)
        self.data.append(self.y_large)
        self.data.append(self.w_large)
        self.data.append(self.h_large)

    def drawBoundingbox(self):
        """ 
        Draw the bounding box with largest areal onto the img/frame
        Returns:
            Output image with the bounding box drawn        
        """
        self.output_img = cv2.rectangle(self.original, (self.x_large, self.y_large), (self.x_large + self.w_large, self.y_large + self.h_large), (0,255,0), 2)
        cv2.imwrite("/home/frederike/Desktop/bb.png", self.output_img)

        return self.output_img

    def dataOutput(self):
        return self.data

    def create_data_file(self,rois):
        print()
        header = ['Lap Nr']
        roi = 0
        while True:
            if roi < rois:
                header.append('Roi'+str(roi+1))
                header.append('Roi'+str(roi+1)+'_x')
                header.append('Roi'+str(roi+1)+'_y')
                header.append('Roi'+str(roi+1)+'_w')
                header.append('Roi'+str(roi+1)+'_h')
                roi += 1
            else:
                break

        with open('BB-BIG-10-Malfunction.csv', 'w', encoding='UTF8', newline='') as f:      ############################3333
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            f.close()


    def save_data(self, frame_nr):
        self.data.insert(0, frame_nr)
        with open("BB-BIG-10-Malfunction.csv", 'a', encoding='UTF8', newline='') as f:      ################################
            writer = csv.writer(f)
            # write data row
            writer.writerow(self.data)
            self.data.clear()
            f.close()

bb = BoundingBox(3)
img = cv2.imread("/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/singleSpring.jpg")
bb.applyBoundingBox(img)
bb.drawBoundingbox()