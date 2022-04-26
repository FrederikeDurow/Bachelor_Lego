import CentroidTracker
#from imutils.video import VideoStream
import numpy as np
import cv2
import time
from collections import OrderedDict

import Object_Color_Detector as Object_Color_Detector
#import imutils

ct = CentroidTracker.centroidTracker()

(H, W) = (None,None)

print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
# "/home/rasmus/Desktop/Test Videos/Test/20-04/Side (2).mp4"
#"/home/rasmus/Desktop/Test Videos/Test/20-04/Sideblocked (2).mp4"
#output  =cv2.VideoWriter("Object_tracker_2.avi", cv2.VideoWriter_fourcc(*'MPEG'), 100, (1456,1088))
vs = cv2.VideoCapture("/home/rasmus/Desktop/Test Videos/Test/20-04/Sideblocked (2).mp4")
time.sleep(2.0)

ret, init_frame = vs.read()

#confidence = 1

while True:
  roi = cv2.selectROI('Multi Tracker', init_frame)
  print('Press S to start tracking')
  print('Press any other key to select the next object')
  k = cv2.waitKey(0) & 0XFF
  if k == 115: 
    Col_detect = Object_Color_Detector.obj_color_dectector()
    break

while True:

    ret, frame = vs.read()
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    crop_img = blurred[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]
    #frame = imutils.resize(frame, width= 400)

    #if W is None or H is None:
     #   (H, W) = frame.shape[:2]

    # SHOULD BE OUR OWN DETECTOR (MAYBE COLOR DETECTOR) (SHOULD JUST RETURN BOUNDING BOXES)
    detections = Col_detect.applyColorDectector(crop_img)
    print (detections)
    rects = []
    if  detections is not None:
        for i in range(0, len(detections)):
            #if detections[i] > confidence:

                #box = detections[0,0,i, 3:7] * np.array([W,H,W,H])
            rects = detections

            (startX, startY, endX, endY,_) = detections[i]
            cv2.rectangle(crop_img, (startX,startY), (startX+endX, startY+endY), (0,255,0), 2)
            i +=1

    rects = detections      
    print("1:Recs: " + str(len(rects)))
    
        

    objects = ct.update(rects)
    if objects is not None:
        print("Objects: " + str(len(objects)))
        print("Recs: " + str(len(rects)))

        for (objectID, centroid) in objects.items():
            text = "ID {}".format(objectID)
            cv2.putText(crop_img, text, (centroid[0]-10, centroid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
            cv2.circle(crop_img, (centroid[0], centroid[1]), 4, (0,0,255), -1)

    frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]] = crop_img
    #output.write(frame) 
    cv2.imshow("Frame", crop_img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()