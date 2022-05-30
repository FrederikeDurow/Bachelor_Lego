import cv2
import numpy as np

class obj_color_dectector():
    
    frame = None
    output_img = None

    countours = None 
    data = []

    HSV_lower = None
    HSV_upper = None
    
    def __init__(self):
        pass

    def applyColorDectector(self, frame,hsv_low, hsv_up, size):                                             
        self.HSV_lower = hsv_low
        self.HSV_upper = hsv_up
        self.data.clear()
        self.frame = frame
        hsv_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        if self.HSV_lower != None:
            mask = cv2.inRange(hsv_frame, self.HSV_lower, self.HSV_upper)
            kernel = np.ones((5, 5), "uint8")

            mask = cv2.dilate(mask, kernel)

            self.countours, self.hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for c in self.countours:
                x,y,w,h = cv2.boundingRect(c)
                area = (w)*(h)
                bounding = [x,y,w,h,area]
                if area > size:
                    self.data.append(bounding)
            return self.data
        else:
            print("Use HSV_Trackbar to set upper and lower bounds")