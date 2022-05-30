import cv2

class BoundingBox():
    
    img = None
    countours = None
    output_img = None

    def __init__(self):
        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0
        self.data = []

    def applyBoundingBox(self,image):
        self.img = image
        gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        self.contours =  cv2.findContours(thresh_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2]

        self.w_large = 0
        self.h_large = 0
        self.x_large = 0
        self.y_large = 0

        for c in self.contours:
            x,y,w,h = cv2.boundingRect(c)
            if w*h > self.w_large*self.h_large:
              self.w_large = w
              self.h_large = h
              self.x_large = x
              self.y_large = y
        self.addData()
    
    def addData(self):
        self.data.append([self.x_large,self.y_large,self.w_large,self.h_large])

    def drawBoundingbox(self):
        self.output_img = cv2.rectangle(self.img, (self.x_large, self.y_large), (self.x_large + self.w_large, self.y_large + self.h_large), (0,255,0), 2)
        return self.output_img

    def getData(self):
        return self.data
    
    def clearData(self):
        self.data = []
