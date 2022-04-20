import cv2 #openCV
import sys #OS functions
from random import randint #random numbers

#List of tracking algorithms
tracking_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
tracking_type = tracking_types[2]
print(tracking_type)

if tracking_type == 'BOOSTING':
    tracker = cv2.legacy.TrackerBoosting_create()
elif tracking_type == 'MIL':
    tracker = cv2.legacy.TrackerMIL_create()
elif tracking_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()
elif tracking_type == 'TLD':
    tracker = cv2.legacy.TrackerTLD_create()
elif tracking_type == 'MEDIANFLOW':
    tracker = cv2.legacy.TrackerMedianFlow_create()
elif tracking_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()
elif tracking_type == 'CSRT':
    tracker = cv2.legacy.TrackerCSRT_create()

print(tracker)

#Open video & print error message if video was not opened
testVid = cv2.VideoCapture('/home/rasmus/Desktop/Test Videos/07-04/Big Springs/50-Correct-Laps.mp4')
if not testVid.isOpened():
    print('Video was not loaded')
    sys.exit()

#Get first frame of the video to choose the object to be tracked (in a bounding box)
#We always make to variables, the first is ta boolean which indicates if the second variable was loaded
ret, frame = testVid.read()
if not ret:
    print('Error while loading frame')
    sys.exit()

#select region of interest
roi = cv2.selectROI(frame)
print(roi) #this will show us the coordinates for the upper left corner followed by the size 

#Initializing the chosen detection algorithm (tracker) to track the ROI
ret = tracker.init(frame,roi)
print(ret)

#Initializing a random BGR color, used to track multiple bounding boxes
colors = (randint(0, 255), randint(0,255), randint(0,255))
print(colors)

#going through all frames to actually track the object
while True: 
    ret, frame = testVid.read()
    #When the video endend, stop tracking:
    if not ret:
        break
    ret, roi = tracker.update(frame)
    #print(ret, roi)
    
    #Drawing roi with updated position on the newest frame
    if ret == True:
            (x, y, w, h) = [int(v) for v in roi]
            cv2.rectangle(frame, (x,y), (x+w, y+h), colors, 4)
    else: 
        cv2.putText(frame, 'Tracking failure!', (100,80), cv2.FONT_HERSHEY_SIMPLEX, .75, (0,0,255), 2)

    cv2.putText(frame, tracking_type, (100,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
    cv2.imshow('Tracking Test', frame)
    if cv2.waitKey(1) & 0xFF == 27: #when escape is pressed
        break

