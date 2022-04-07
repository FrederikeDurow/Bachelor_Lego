import numpy as np
import cv2 as cv

# KNN and BBS work with video file
# BBS not implemented as it is based on the webcam for the moment

class BackgroundSubstractor():

    cap = None

    bg_substractor = None
    erode_kernel = None
    dilate_kernel = None

    def __init__(self, type):
        if type.upper() == 'BBS':
            self.type = 'BBS'
            print('Basic Background Substractor selected')
        elif type.upper() =='MOG2':
            self.type = 'MOG2'
            self.bg_substractor = cv.createBackgroundSubtractorMOG2(detectShadows=True)
            self.erode_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
            self.dilate_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,7))
            print('MOG2 Background Substractor selected')
        elif type.upper() == 'KNN':
            self.type = 'KNN'
            self.bg_substractor = cv.createBackgroundSubtractorKNN(detectShadows=True)
            self.erode_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7,5))
            self.dilate_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (17,11))
            print('KNN Background Substractor selected')
        else:
            print('Please use proper type: FAST or SHI THOMASI')

    def applyBackgroundSubstractor(self, video):
        if self.type =='BBS':
            pass

        elif self.type == 'KNN' or self.type =='MOG2':
            cap =cv.VideoCapture(video)
            success, frame = cap.read()

            while success:
                fg_mask = self.bg_substractor.apply(frame)

                _, thresh = cv.threshold(fg_mask, 244, 255, cv.THRESH_BINARY)
                cv.erode(thresh, self.erode_kernel,thresh, iterations=2)
                cv.dilate(thresh, self.dilate_kernel, thresh, iterations=2)

                contours, hier = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

                for c in contours:
                    if cv.contourArea(c) > 1000:
                        x,y,w,h = cv.boundingRect(c)
                        cv.rectangle(frame, (x,y), (x+w, y+h), (255,255,0), 2)

                cv.imshow('Mog',fg_mask)
                cv.imshow('Thresh',thresh)
                cv.imshow('Detecton', frame)
                
                k = cv.waitKey(30)
                if k == 27: #Escape
                    cv.destroyAllWindows()
                    break

                success,frame = cap.read()

 ## --------------------- How to use---------------------:

 # 1. One video needed (should be from another class)
video1 = 'slow_traffic_small.mp4'

 # 2. Create a BacgroundSubstractor object (BBS or MOG2 or KNN)
test = BackgroundSubstractor('KNN')

 # 3. Apply detector (first is the template, the other is the one to check on)¨
test.applyBackgroundSubstractor(video1)

