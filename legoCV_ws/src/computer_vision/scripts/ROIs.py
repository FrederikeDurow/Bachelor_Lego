import numpy as np
import cv2

class ROIs:

   def choose_rois(self):
        print("Select a new ROI by clicking on its desired upper left corner and lower right corner position")
        while True:
            if self.roi_added == 0:

                cv2.setMouseCallback('Camera Live Stream', self.new_roi)
            else:
                print("Press 'd' to delete the last ROI")
                print("Press 'r' to select another ROI")
                print("Press any other key to select the next object")

                key = input()
                if key == "d":
                    #Delete
                    break
                elif key == "r":
                    self.roi_added = 0
                else:
                    break

    def new_roi(self, event,x,y,flags,params):
        
        if (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 0):
            self.temp_roi = []
            
            self.temp_roi.append(x)
            self.temp_roi.append(y)
            print("1")
            print(self.temp_roi)
            self.roi_state = 1
            print("State if: ")
            print(self.roi_state)


        elif (event == cv2.EVENT_LBUTTONUP) and (self.roi_state == 1):
            print("nr2")
            self.temp_roi.append(x-self.temp_roi[0])
            self.temp_roi.append(y-self.temp_roi[1])
            self.rois.append(self.temp_roi)
            self.roi_state = 0
            self.roi_added = 1 
            print("State elif: ")
            print(self.roi_state)


    def draw_rois(self):
        print("rois")
        print(self.rois)
        if len(self.rois) > 0:
            self.current_frame = cv2.cvtColor(self.current_frame, cv2.COLOR_GRAY2BGR)
            for roi in self.rois:
                if len(roi) == 4:
                    cv2.rectangle(self.current_frame, (roi[0], roi[1]), (roi[0]+roi[2] , roi[1]+roi[3]), (0,255,0), 2)
    
