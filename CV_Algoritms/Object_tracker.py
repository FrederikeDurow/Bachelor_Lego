import CentroidTracker
#from imutils.video import VideoStream
import numpy as np
import cv2
import time
#import imutils
import Multi_Color_Dectector

ct = CentroidTracker.centroidTracker()

(H, W) = (None,None)

print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = cv2.VideoCapture(0)
time.sleep(2.0)

Col_detect = Multi_Color_Dectector.multi_color_dectector()
confidence = 0.5

while True:

    frame = vs.read()
    #frame = imutils.resize(frame, width= 400)

    #if W is None or H is None:
     #   (H, W) = frame.shape[:2]

    # SHOULD BE OUR OWN DETECTOR (MAYBE COLOR DETECTOR) (SHOULD JUST RETURN BOUNDING BOXES)
    detections = Col_detect.applyColorDectector(frame)
    rects = []

    for i in range(0, detections.shape[2]):
        if detections[0,0,i,2] > confidence:

            box = detections[0,0,i, 3:7] * np.array([W,H,W,H])
            rects.append(box.astype("int"))

            (startX, startY, endX, endY) = box.astype("int")
            cv2.rectangle(frame, (startX,startY), (endX, endY), (0,255,0), 2)

    objects = ct.update(rects)

    for (objectID, centroid) in objects.items():

        text = "ID {}".format(objectID)
        cv2.putText(frame, text, (centroid[0]-10, centroid[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
        cv2.circle(frame, (centroid[0], centroid[1]), 4, (0,255,0), -1)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cv2.destroyAllWindows()
vs.stop()