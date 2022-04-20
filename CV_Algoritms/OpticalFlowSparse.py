import numpy as np
import cv2
import csv

vidCap = cv2.VideoCapture("C:/Users/rasm4/OneDrive - Syddansk Universitet (1)/Desktop/Test/20-04/TopView.mp4")
output  =cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*'MPEG'), 30, (1456,1088))

ret, frame = vidCap.read()
init_frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(init_frame_gray, (11, 11), 0)
corners = cv2.goodFeaturesToTrack(blurred,20,0.1,10)
cv2.imshow('Blurred', blurred)

corners = np.int0(corners)

output_img = frame
output_img[corners > 0.01 * corners.max()] =[0,0,255]

parameters_lucas_kanade = dict(winSize = (15,15), maxLevel = 2, criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
diso = cv2.DISOpticalFlow_create(cv2.DISOpticalFlow_PRESET_MEDIUM)

header = ['Lap Nr', 'Point 1', 'X', 'Y']
with open('Point Tracking.csv', 'w', encoding='UTF8', newline='') as f:      ############################3333
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            f.close()

def select_point(event, x, y, flags, params):
    global point, selected_point, old_points
    if event == cv2.EVENT_LBUTTONDOWN: #if left mouse button pressed
        point = (x, y)
        selected_point = True
        old_points = np.array([[x,y]], dtype=np.float32)

#cv2.namedWindow('Current frame')
#cv2.setMouseCallback('Current frame', select_point)

selected_point = False
point = ()
old_points = np.array([[]])
mask = np.zeros_like(frame)
frame_counter = 0

while True:

    cv2.namedWindow('Current frame')
    cv2.imshow('Current frame', frame)
    cv2.setMouseCallback('Current frame', select_point)
    print('Press S to start tracking')

    k = cv2.waitKey(0) & 0XFF
    if k == 115: 
      break

while True:
    ret, frame = vidCap.read()
    frame_counter +=1
    if not ret:
        break
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if selected_point is True:
        cv2.circle(frame, point, 5, (0,0 , 255), 2)

        new_points, status, errors = cv2.calcOpticalFlowPyrLK(init_frame_gray, frame_gray, old_points, None, **parameters_lucas_kanade)

        init_frame_gray = frame_gray.copy()
        old_points = new_points

        #Current and next location
        x, y = new_points.ravel()
        j, k = old_points.ravel()

        data = [frame_counter,0,x,y]
        with open("Point Tracking.csv", 'a', encoding='UTF8', newline='') as f:      ################################
            writer = csv.writer(f)
            # write data row
            writer.writerow(data)

        cv2.putText(frame, "dx: {}, dy: {}".format(x, y),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,
		0.35, (0, 255, 0), 1)
    
        mask = cv2.line(mask, (int(x),int(y)), (int(j),int(k)), (0, 255, 255), 2)
        frame = cv2.circle(frame, (int(x),int(y)), 5, (0, 255, 0), -1)

    output.write(frame) 
    #Img is the frame with added path's and circles
    img = cv2.add(frame, mask)
    cv2.imshow('Current frame', img)
    #cv2.imshow('Only edges and their path', mask)
    
    key = cv2.waitKey(30)
    if key == 27: # enter
        break 

