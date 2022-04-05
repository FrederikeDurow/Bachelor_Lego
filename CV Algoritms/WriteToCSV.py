import csv
import cv2
import numpy
import sys #OS functions
from random import randint #random numbers

def Histogram(image):
    image1  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histo = cv2.calcHist([image1],[0],None,[256],[0,256])
    


def boundingBox(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        print("nyt image")
        print(c)
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,0), 2)
    cv2.imshow("test", image)
    cv2.waitKey(0)
    return image

# cv2.imwrite("test1.jpg",frame)
# roi_img = boundingBox(cv2.imread('test1.jpg'))


def main():
    
    # READING THE VIDEO INPUT

    cap = cv2.VideoCapture("Test/31-03/31-03-Test1.mp4")
    output = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'MP4V'), 100, (1456, 1088))
   
    if not cap.isOpened():
        print('Video was not loaded')
        sys.exit()

    ret, frame = cap.read()

    # CREATE MULTIPLE ROI REGIONS

    rois = []
    colors = []

    while True:
        roi = cv2.selectROI('Multi Tracker', frame)
        rois.append(roi)
        colors.append((randint(0, 255), randint(0,255), randint(0,255)))

        print('Press S to start tracking')
        print('Press any other key to select the next object')

        k = cv2.waitKey(0) & 0XFF
        if k == 115: 
            break
    
    # Elements =[]
    # for roi in rois: 
    #   Elements.append(cv2.rectangle(frame,()))

    # GOES THROUGH THE VIDEO AND APPLY 
  
    while(True):
        ret, frame = cap.read()
        if(ret):
              
            # DO SOMETING TO ROIS
            for roi in rois:
                cv2.rectangle(frame, (roi[0],roi[1]) , (roi[0]+roi[2], roi[1]+roi[3]), (0,255,0), 2)
                roi_img = frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]]
                
                # Alogoritm here
                cv2.imwrite("test1.jpg",frame)
                roi_img = boundingBox(cv2.imread('test1.jpg'))

                # Conversion for 3 channels to put back on original image
                roi_img_rgb = cv2.cvtColor(roi_img,cv2.COLOR_BGR2GRAY)
                roi_img_rgb = cv2.cvtColor(roi_img_rgb,cv2.COLOR_GRAY2BGR)
                frame[roi[1] : roi[1]+roi[3], roi[0] : roi[0]+roi[2]] = roi_img_rgb

            # writing the new frame in output
            output.write(frame)
            cv2.imshow("output", frame)
            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
        else:
            break
  
    cv2.destroyAllWindows()
    output.release()
    cap.release()
  
  
if __name__ == "__main__":
    main()

main()
#
#
#header = ['Frame nr', 'area', 'country_code2', 'country_code3']
#data = [
#    ['Albania', 28748, 'AL', 'ALB'],
#    ['Algeria', 2381741, 'DZ', 'DZA'],
#    ['American Samoa', 199, 'AS', 'ASM'],
#    ['Andorra', 468, 'AD', 'AND'],
#    ['Angola', 1246700, 'AO', 'AGO']
#]
#
#with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
#    writer = csv.writer(f)
#
#    # write the header
#    writer.writerow(header)
#
#    # write multiple rows
#    writer.writerows(data)