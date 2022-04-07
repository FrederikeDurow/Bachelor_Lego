import numpy as np
import cv2 as cv

class CornerDetector ():

    img = None
    corners = None

    output_img = None

    data = []

    def __init__(self, type):

        if type.upper() == 'FAST':
            self.type = 'FAST'
            print('FAST Corner Detector selected')
        elif type.upper() =='SHI TOMASI':
            self.type = 'SHI TOMASI'
            print('Shi-Tomasi Corner Detector selected')
        else:
            print('Please use proper type: FAST or SHI THOMASI')

    def applyCornerDetector(self, img):

        self.img = img
        gray_img = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

        if self.type =='FAST':
            gray_img = np.float32(gray_img)
            self.corners = cv.cornerHarris(gray_img, 2, 5, 0.07)
            self.corners = cv.dilate(self.corners, None)

        elif self.type == 'SHI TOMASI':
            self.corners = cv.goodFeaturesToTrack(gray_img,25,0.01,10)
            self.corners = np.int0(self.corners)

    def showCorners(self):

        if self.type =='FAST':
            self.output_img = self.img
            self.output_img[self.corners > 0.01 * self.corners.max()] =[0,0,255]

        elif self.type == 'SHI TOMASI':
            self.output_img = self.img
            for i in self.corners:
                x,y = i.ravel()
                cv.circle(self.output_img,(x,y),3,255,-1)

        cv.imshow('Corners', self.output_img)
        cv.waitKey(0)

    def add_data(self):
        for corners
        self.data.append('')
        self.data.append(self.corners.size)
        self.data.append(self.corners.)

    def dataoutput(self):
        return self.data

    def create_data_file(self,rois):
        header = ['Lap Nr:']
        roi_cnt = 1
        corner_cnt = 1
        for roi in rois:
            header.append('Roi'+str(roi_cnt))
            for corner in self.corners:
                header.append('Corner'+str(corner_cnt))
                header.append('Amount')
                header.append('x')
                header.append('y')
                corner_cnt +=1
            roi_cnt +=1





## --------------------- How to use---------------------:

# 1. Two image needed (should be from another class (ROI))
#img1 = cv.imread('lego.jpg') # Original image

# 2. Create CornerDetector object (should be based on ROI at some point)
#obj = CornerDetector('SHI TOMASI')

# 3. Apply corner detector
#obj.applyCornerDetector(img1)

# 4. Show result
#obj.showCorners()