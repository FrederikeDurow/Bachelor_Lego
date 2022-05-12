import cv2
import numpy as np


class obj_color_dectector():
    
    frame = None
    output_img = None

    countours = None 
    data = []
    # countours_red = None
    # countours_green = None
    # countours_blue = None

    # data_red = []
    # data_green = []
    # data_blue = []

    HSV_lower = None
    HSV_upper = None

    #ADD MORE LOWER/UPPER FOR MORE COLORS
    
    def __init__(self):
        pass
        # self.red = (0, 0, 255)
        # self.green = (0, 255, 0)
        # self.blue  = (255, 0, 0)

    def applyColorDectector(self, frame,hsv_low, hsv_up, size):                                             #We need to hardcode size
        #self.color = color
        self.HSV_lower = hsv_low
        self.HSV_upper = hsv_up
        self.data.clear()
        self.frame = frame
        hsvFrame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

    
        if self.HSV_lower != None:
            mask = cv2.inRange(hsvFrame, self.HSV_lower, self.HSV_upper)
        
            # Morphological Transform, Dilation
            # for each color and bitwise_and operator
            # between imageFrame and mask determines
            # to detect only that particular color
            kernel = np.ones((5, 5), "uint8")

            mask = cv2.dilate(mask, kernel)
            #res= cv2.bitwise_and(self.frame, self.frame, mask)

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

#     def HSV_Trackbar(self, frame):

#         self.frame = frame

#         cv2.namedWindow('frame')

#         # Create trackbars for color change
#         # Hue is from 0-179 for Opencv
#         cv2.createTrackbar('Hue_Min', 'frame', 0, 179, nothing)
#         cv2.createTrackbar('Sat_Min', 'frame', 0, 255, nothing)
#         cv2.createTrackbar('Val_Min', 'frame', 0, 255, nothing)
#         cv2.createTrackbar('Hue_Max', 'frame', 0, 179, nothing)
#         cv2.createTrackbar('Sat_Max', 'frame', 0, 255, nothing)
#         cv2.createTrackbar('Val_Max', 'frame', 0, 255, nothing)

#         # Set default value for Max HSV trackbars
#         cv2.setTrackbarPos('Hue_Max', 'frame', 179)
#         cv2.setTrackbarPos('Sat_Max', 'frame', 255)
#         cv2.setTrackbarPos('Val_Max', 'frame', 255)

#         # Initialize HSV min/max values
#         hMin = sMin = vMin = hMax = sMax = vMax = 0
#         phMin = psMin = pvMin = phMax = psMax = pvMax = 0

#         while(True):
#             # Get current positions of all trackbars
#             hMin = cv2.getTrackbarPos('Hue_Min', 'frame')
#             sMin = cv2.getTrackbarPos('Sat_Min', 'frame')
#             vMin = cv2.getTrackbarPos('Val_Min', 'frame')
#             hMax = cv2.getTrackbarPos('Hue_Max', 'frame')
#             sMax = cv2.getTrackbarPos('Sat_Max', 'frame')
#             vMax = cv2.getTrackbarPos('Val_Max', 'frame')

#             # Set minimum and maximum HSV values to display
#             self.HSV_lower = np.array([hMin, sMin, vMin])
#             self.HSV_upper = np.array([hMax, sMax, vMax])

#             # Convert to HSV format and color threshold
#             hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#             mask = cv2.inRange(hsv, self.HSV_lower, self.HSV_upper)
#             result = cv2.bitwise_and(frame, frame, mask=mask)

#             # Print if there is a change in HSV value
#             if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
#                 print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
#                 phMin = hMin
#                 psMin = sMin
#                 pvMin = vMin
#                 phMax = hMax
#                 psMax = sMax
#                 pvMax = vMax

#             # Display result image
#             cv2.imshow('image', result)
#             print("\n[USER INPUT] Press 's' to save chosen threshold")
#             # if key == "d":
#             #     self.rois.pop()
#             # elif key == "s":
#             #     break
#             if cv2.waitKey(10) & 0xFF == ord('s'):
#                 cv2.destroyAllWindows()
#                 return self.HSV_lower, self.HSV_upper

        

# def nothing(x):
#     pass

# self.frame = frame
#         if self.color == "r":
#             self.redDetector()
#         elif self.color == "g":
#             self.greenDetector()
#         else:
#             self.blueDetector()