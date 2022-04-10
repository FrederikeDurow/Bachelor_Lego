from cv2 import cornerSubPix
import numpy as np
import csv
import cv2 as cv

class CornerDetector ():

    img = None
    corners = None

    output_img = None

    data = []

    def __init__(self, type, rois):
        self.objects = rois
        
        self.current_object = 0
        if type.upper() == 'FAST':
            self.type = 'FAST'
            print('FAST Corner Detector selected')
        elif type.upper() =='SHI TOMASI':
            self.type = 'SHI TOMASI'
            print('Shi-Tomasi Corner Detector selected')
        else:
            print('Please use proper type: FAST or SHI THOMASI')
        self.create_data_file()


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
            self.add_data()


    def drawCorners(self):

        if self.type =='FAST':
            self.output_img = self.img
            self.output_img[self.corners > 0.01 * self.corners.max()] =[0,0,255]

        elif self.type == 'SHI TOMASI':
            self.output_img = self.img
            for i in self.corners:
                x,y = i.ravel()
                cv.circle(self.output_img,(x,y),3,255,-1)

        return self.output_img

    def dataoutput(self):
        return self.data

    

    def create_data_file(self):
        o = 0
        while True:
            if o < self.objects:
                header = [('Object nr ' + str(o+1)), 'Lap Nr:']
                header.append('Nr. of Corners')
                header.append('Corner 1')
                header.append('x')
                header.append('y')
            
                with open('CD-Cannon-'+str(o+1)+'.csv', 'w', encoding='UTF8', newline='') as f:         #######################33
                    writer = csv.writer(f)

                    # write the header
                    writer.writerow(header)
                    f.close()
                o += 1
            else:
                break


    def add_data(self):
        self.data.append('')
        self.data.append(len(self.corners))
        cnt = 1
        for corner in self.corners:
            x,y = corner.ravel()
            self.data.append('C ' + str(cnt))
            self.data.append(x)
            self.data.append(y)
            cnt += 1

    def save_data(self, frame_nr):
        if self.current_object < self.objects:
            self.current_object +=1
        else:
            self.current_object = 1

        self.data.insert(1, frame_nr)
        with open('CD-Cannon-'+str(self.current_object)+'.csv', 'a', encoding='UTF8', newline='') as f:         ########################
            writer = csv.writer(f)
            # write data row
            writer.writerow(self.data)
            self.data.clear()
            f.close()


## --------------------- How to use---------------------:

# 1. Two image needed (should be from another class (ROI))
#img1 = cv.imread('lego.jpg') # Original image

# 2. Create CornerDetector object (should be based on ROI at some point)
#obj = CornerDetector('SHI TOMASI')

# 3. Apply corner detector
#obj.applyCornerDetector(img1)

# 4. Show result
#obj.showCorners()