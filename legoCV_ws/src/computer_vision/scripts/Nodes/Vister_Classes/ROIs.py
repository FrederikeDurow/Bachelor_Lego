import numpy as np
import cv2

class ROIs:

    def __init__(self, windowName, image):
        self.window_name = windowName
        self.current_image = image
        self.temp_roi = []
        self.rois = []
        self.roi_state = 0
        self.roi_added = 0
        self.roi_chosen = False
   

    def get_rois(self):
        return self.rois

    def set_multi_rois(self):
        print("Select a region by clicking on its upper left corner followed by lower right corner.")
        cv2.setMouseCallback(self.window_name, self.add_roi)
        while True: 
            if self.roi_chosen == True:
                key = input("\n[USER INPUT] Do you want to:\n'd' - delete last region\n'r' - select another region \n's' - save chosen regions\n")
                if key == "d":
                    self.rois.pop()
                elif key == "r":
                    self.roi_added = 0
                    self.roi_chosen = False
                    print("\n[MSG] Please select the next region.")
                elif key == "s":
                    break
                else:
                    pass

    def set_single_roi(self):
        print("Select a region by clicking on its upper left corner followed by lower right corner.")
        cv2.setMouseCallback(self.window_name, self.add_roi)
        while True: 
            if self.roi_chosen == True:
                key = input("\n[USER INPUT] Do you want to:\n'd' - delete last region\n's' - save chosen region\n")
                if key == "d":
                    self.rois.pop()
                elif key == "s":
                    break
                else:
                    print("[MSG] The pressed key is not an option.")

    def add_roi(self, event,x,y,flags,*params):
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.set_upperleft(x,y)   
        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            self.set_lowerright(x,y)
        else: 
            pass

    def set_upperleft(self, x, y):
        self.temp_roi = []
        self.temp_roi.append(x)
        self.temp_roi.append(y)
        self.roi_chosen = True
        self.roi_state = 1
        pass


    def set_lowerright(self, x, y):
        self.temp_roi.append(x-self.temp_roi[0])
        self.temp_roi.append(y-self.temp_roi[1])
        self.rois.append(self.temp_roi)
        self.roi_state = 0
        self.roi_added = 1 
        pass


    def draw_rois(self, image):
        if len(self.temp_roi) > 0:
            cv2.circle(image, (self.temp_roi[0],self.temp_roi[1]), 2, (0,255,0), -1)
        for roi in self.rois:
            cv2.rectangle(image, (roi[0], roi[1]), (roi[0]+roi[2] , roi[1]+roi[3]), (0,255,0), 2)
        return image
