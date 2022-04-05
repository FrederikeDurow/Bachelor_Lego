import numpy as np
from random import randint 
import sys
import cv2

#Get the camera live stream 
live_vid = cv2.VideoCapture('Media/media1.mp4') 
if not live_vid.isOpened():
    print('No camera detected')
    sys.exit()

ret, frame = live_vid.read()
init_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#Initialize Trackers (both KCF for region of interest and optical flow for point)
roi_tracker = cv2.legacy.TrackerKCF_create()
para_lucas_kanade = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

#We will store bounding box data and random colors in arrays, since we want to track multiple objects
rois = []
colors = []

cv2.namedWindow('Point & ROI Tracking')
#Setup for choosing points to track
def select_point(event, x, y, flags, params):
    global point, selected_point, old_points
    if event == cv2.EVENT_LBUTTONDOWN: #if left mouse button pressed
        point = (x, y)
        selected_point = True
        old_points = np.array([[x,y]], dtype=np.float32)

#Show initial frame to select regions and points of interest
while True:
    roi = cv2. selectROI('Point & ROI Tracking', frame)
    rois.append(roi)
    colors.append((randint(0, 255), randint(0,255), randint(0,255)))
    
    #print('Press S to start tracking')
    print('Press P to choose single points to track')
    print('Press any other key to select the next object')

    # If P is pressed
    k = cv2.waitKey(0) & 0XFF
    if k == 112:
        break

#Choose tracker for every region of interest 
multi_tracker = cv2.legacy.MultiTracker_create()
for roi in rois: 
    multi_tracker.add(cv2.legacy.TrackerKCF_create(), frame, roi)

#Choose single points to track:
print('Select a point to track by clicking on it')

cv2.setMouseCallback('Point & ROI Tracking', select_point)

selected_point = False
point = ()
old_points = np.array([[]])
mask = np.zeros_like(frame)

while True:
    ret, frame = live_vid.read()
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if selected_point is True:
        cv2.circle(frame, point, 5, (0,0,255), 2)

        #Begin to track point, from the old gray scale frame to the new one
        new_points, status, errors = cv2.calcOpticalFlowPyrLK(init_frame_gray, frame_gray, old_points, None, **para_lucas_kanade)


        init_frame_gray = frame_gray.copy()
        old_points = new_points

        #Current and next location
        x, y = new_points.ravel()
        j, k = old_points.ravel() 

        mask = cv2.line(mask, (int(x),int(y)), (int(j),int(k)), (0, 255, 255), 2)
        frame = cv2.circle(frame, (int(x),int(y)), 5, (0, 255, 0), -1)


    #Update regions of interest
    ret, rois = multi_tracker.update(frame)
    #draw all regions of interest at their updated position
    for i, new_roi in enumerate(rois):
        (x, y, w, h) = [int(v) for v in new_roi]
        cv2.rectangle(frame, (x,y), (x + w, y + h), colors[i], 4)

    #Img is the frame with added path's and circles
    img = cv2.add(frame, mask)
    cv2.imshow('Point & ROI Tracking', img)
 
    cv2.waitKey(30)

