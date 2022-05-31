import cv2

class ROIs:

    def __init__(self, windowName):
        self.window_name = windowName
        self.temp_roi = []
        self.rois = []
        self.roi_state = 0
        self.roi_added = 0
        self.roi_chosen = False
   
    def getRois(self):
        return self.rois

    def setMultiRois(self):
        print("Select a region by clicking on its upper left corner followed by lower right corner.")
        cv2.setMouseCallback(self.window_name, self.addRoi)
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

    def setSingleRoi(self):
        print("Select a region by clicking on its upper left corner followed by lower right corner.")
        cv2.setMouseCallback(self.window_name, self.addRoi)
        while True: 
            if self.roi_chosen == True:
                key = input("\n[USER INPUT] Do you want to:\n'd' - delete last region\n's' - save chosen region\n")
                if key == "d":
                    self.rois.pop()
                elif key == "s":
                    break
                else:
                    print("[MSG] The pressed key is not an option.")

    def addRoi(self, event,x,y,flags,*params):
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.setUpperLeft(x,y)   
        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            self.setLowerRight(x,y)
        else: 
            pass

    def setUpperLeft(self, x, y):
        self.temp_roi = []
        self.temp_roi.append(x)
        self.temp_roi.append(y)
        self.roi_chosen = True
        self.roi_state = 1
        pass


    def setLowerRight(self, x, y):
        self.temp_roi.append(x-self.temp_roi[0])
        self.temp_roi.append(y-self.temp_roi[1])
        self.rois.append(self.temp_roi)
        self.roi_state = 0
        self.roi_added = 1 
        pass


    def drawRois(self, image):
        if len(self.temp_roi) > 0:
            cv2.circle(image, (self.temp_roi[0],self.temp_roi[1]), 2, (0,255,0), -1)
        for roi in self.rois:
            cv2.rectangle(image, (roi[0], roi[1]), (roi[0]+roi[2] , roi[1]+roi[3]), (0,255,0), 2)
        return image
