import cv2
import numpy


class CannyEdgeDetector():
    
    edges = None
    
    def __init__(self, img):
        self.img = img
        self.blur_img = cv2.GaussianBlur(self.img,(3,3),0)

    def applyCanny(self, threshold1=100, threshold2=200):
        self.edges = cv2.Canny(self.blur_img, threshold1, threshold2)

    def showEdges(self):
        self.edges = cv2.resize(self.edges, (1280,720))
        cv2.imshow('Matches', self.edges)
        cv2.waitKey(0)

 ## --------------------- How to use---------------------:

 # 1. One image needed (should be from another class (ROI))
img1 = cv2.imread('soccer.jpg') # Original image

 # 2. Create a CannyEdgeDetector object
test = CannyEdgeDetector(img1)

 # 3. Apply detector (default values threshold1 =100, threshold2 =200) 
test.applyCanny()

 # 5. Draw matches
test.showEdges()