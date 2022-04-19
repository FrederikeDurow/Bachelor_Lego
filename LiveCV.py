import csv
from cv2 import imshow
import numpy as np
import cv2
import sys
# sys.path.insert(0,'/home/frederike/Documents/SDU-Robotics/Bachelor/Bachelor_Lego/CV_Algoritms')
sys.path.insert(0, 'C:/LEGO/Bachelor_Lego')
from CV_Algoritms import CornerDetector as cd
from CV_Algoritms import BoundingBox as bb
 
from random import randint #random numbers

def frame_writer(image, nr):
  cv2.imwrite("frame%d.jpg" % nr, image)


def main():

  
  frame_cnt = 0
  # cap = cv2.VideoCapture("/media/frederike/TOSHIBA EXT/Test/07-04/Big Springs/Light Changes.mp4")    #######################33
  cap = cv2.VideoCapture("C:/Users/rasm4/OneDrive - Syddansk Universitet (1)/Desktop/Test/07-04/Big Springs/10-Malfunction.mp4")
  #output  =cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 100, (1456,1088))
  if not cap.isOpened():
    print('Video was not loaded')
    sys.exit()

  ret, init_frame = cap.read()

  # SELECT ALL REGIONS OF INTEREST
  rois = []
  colors = []

  while True:
    roi = cv2.selectROI('Multi Tracker', init_frame)
    rois.append(roi)
    colors.append((randint(0, 255), randint(0,255), randint(0,255)))

    print('Press S to start tracking')
    print('Press any other key to select the next object')

    k = cv2.waitKey(0) & 0XFF
    if k == 115: 
      #C_D = cd.CornerDetector('SHI TOMASI', len(rois))
      B_B = bb.BoundingBox(len(rois))
      break
    
  # APPLY CHOSEN METHOD TO ALL REGIONS OF INTEREST FOR EACH VIDEO FRAME
  while True:
    
    ret, frame = cap.read()
    frame_cnt += 1
    
    if frame_cnt % 800 == 0:
      data = [frame_cnt]
      cv2.imwrite("frame"+str(frame_cnt)+".jpg",frame)

      for roi in rois:
        crop_img = frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]
        
        
        # BOUNDING BOX
        B_B.applyBoundingBox(crop_img)
        bb_img = B_B.drawBoundingbox()
        # CORNER DETECTION
        #C_D.applyCornerDetector(crop_img)
        #cd_img = C_D.drawCorners()
        #C_D.save_data(frame_cnt)

        # Display the resulting frame
        frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]] = bb_img
        #frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]] = cd_img
        
      B_B.save_data(frame_cnt) 
      
    #output.write(frame)  
    cv2.imshow('Corner detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

main()




# def boundingBox(image):
#   gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#   blur = cv2.GaussianBlur(gray,(5,5),0)
#   #ret, thresh_img = cv2.threshold(blur,91,255,cv2.THRESH_BINARY)
#   thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#   cv2.imshow("thresh",thresh_img)
#   contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]
  
#   w_large = 0
#   h_large = 0
#   x_large = 0
#   y_large = 0
#   for c in contours:
#     x,y,w,h = cv2.boundingRect(c)
#     if w*h > w_large*h_large:
#       w_large = w
#       h_large = h
#       x_large = x
#       y_large = y
  
  # cv2.rectangle(image, (x_large, y_large), (x_large + w_large, y_large + h_large), (0,255,0), 2)
  # data = ['', x_large, y_large, w_large, h_large]
  # return image, data





  # def create_data_file(rois, name):
#   header = ['Lap Nr']
#   roi_cnt = 1
#   for roi in rois:
#     header.append('Roi'+str(roi_cnt))
#     header.append('x')
#     header.append('y')
#     header.append('w')
#     header.append('h')
#     roi_cnt += 1

#   with open('testData.csv', 'w', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)
#     f.close()


# def data_writer(data, name):
#   with open(name, 'a', encoding='UTF8', newline='') as f:
#     writer = csv.writer(f)
#   # write multiple rows
#     writer.writerow(data)
#     f.close()