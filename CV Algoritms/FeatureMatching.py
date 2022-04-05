import cv2 as cv
from cv2 import resize
import numpy
# All combination works, but turning might be needed

class FeatureMatcher():

    Algo = None
    Matcher_obj = None
    temp_img = None
    test_img = None

    gray_temp_img = None
    gray_test_img = None

    keypts_1 = 0
    descrip_1 = 0

    keypts_2 = 0
    descrip_2 = 0

    matches = []
    output_img = None
    
    def __init__(self, type, matcher):
        if type.upper() == 'SIFT' and matcher.upper() == 'BFMATCHER':
            self.type = 'SIFT'
            self.matcher = 'BFMATCHER'
            self.Algo = cv.SIFT_create()
        elif type.upper() == 'ORB' and matcher.upper() == 'BFMATCHER':
            self.type = 'ORB'
            self.matcher = 'BFMATCHER'
            self.Algo = cv.ORB_create()
        elif type.upper() == 'SIFT' and matcher.upper() == 'FLANN':
            self.type = 'SIFT'
            self.matcher = 'FLANN'
            self.minHessian = 400
            self.Algo = cv.SIFT_create(self.minHessian)
        elif type.upper() == 'ORB' and matcher.upper() == 'FLANN':
            self.type = 'ORB'
            self.matcher = 'FLANN'
            self.nfeatures = 500
            self.Algo = cv.ORB_create(self.nfeatures)
        else:
            print('Please use right type: SIFT or ORB with BFMATCHER or FLANN')

    def applyDetector(self, img1, img2):
        # Checks if template image is already set
        if self.temp_img == None:
            self.temp_img = img1
        self.test_img = img2

        # Converts the color to gray
        self.gray_temp_img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
        self.gray_test_img = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

        # Perform detection & computation based on parameters set
        self.keypts_1, self.descrip_1 = self.Algo.detectAndCompute(self.gray_temp_img, None)
        self.keypts_2, self.descrip_2 = self.Algo.detectAndCompute(self.gray_test_img, None)

    def applyMatcher(self):
        if  self.matcher == 'BFMATCHER' and self.type == 'SIFT':
            self.Matcher_obj = cv.BFMatcher(cv.NORM_L1, crossCheck=True)
            self.matches = self.Matcher_obj.match(self.descrip_1,self.descrip_2)
            self.matches = sorted(self.matches, key= lambda match : match.distance)
            print('SIFT & BFMATCHER selected')

        if self.matcher == 'BFMATCHER' and self.type == 'ORB':
            self.Matcher_obj =cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
            self.matches = self.Matcher_obj.match(self.descrip_1,self.descrip_2)
            print('ORB & BFMATCHER selected')

        if self.matcher == 'FLANN' and self.type == 'SIFT':        
            FLANN_INDEX_KDTREE = 1
            index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
            search_params = dict(checks=50) # or pass empty dictionary
            self.Matcher_obj = cv.FlannBasedMatcher(index_params,search_params)
            self.matches = self.Matcher_obj.knnMatch(self.descrip_1,self.descrip_2, k=2)
            print('SIFT & FLANN selected')

        if self.matcher == 'FLANN' and self.type == 'ORB':
            index_params = dict(algorithm=6,
                        table_number=6,
                        key_size=12,
                        multi_probe_level=2)
            search_params = {}
            flann = cv.FlannBasedMatcher(index_params, search_params)
            self.matches = flann.knnMatch(self.descrip_1, self.descrip_2, k=2)
            print('ORB & FLANN selected')

    def drawMatches(self, amount):
        if self.matcher == 'BFMATCHER':
            # add "flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS" if you dont wont points not used
            self.output_img = cv.drawMatches(self.gray_temp_img, self.keypts_1, self.gray_test_img, self.keypts_2, self.matches[:amount],None)
      
        elif self.matcher == 'FLANN':
            matchesMask = [[0,0] for i in range(len(self.matches))]
            # ratio test as per Lowe's paper
            for i,(m,n) in enumerate(self.matches):
                if m.distance < 0.7*n.distance:
                    matchesMask[i]=[1,0]
            draw_params = dict(matchesMask = matchesMask,
                                flags = cv.DrawMatchesFlags_DEFAULT)
            # cv.drawMatchesKnn expects list of lists as matches.
            self.output_img = cv.drawMatchesKnn(self.gray_temp_img,self.keypts_1,self.gray_test_img,self.keypts_2,self.matches,None,**draw_params)

        # resizes the image to 720p
        self.output_img = cv.resize(self.output_img, (1280,720))
        cv.imshow('Matches', self.output_img)
        cv.waitKey(0)


 ## --------------------- How to use---------------------:

 # 1. Two image needed (should be from another class (ROI))
img1 = cv.imread('ball.jpg') # Original image
img2 = cv.imread('soccer.jpg') # Rotated image

 # 2. Create a FeatureMatcher object (SIFT or ORB)
test = FeatureMatcher('ORB', 'FLANN')

 # 3. Apply detector (first is the template, the other is the one to check on)
test.applyDetector(img1, img2)

 # 4. Apply matcher
test.applyMatcher()

 # 5. Draw matches
test.drawMatches(30)


















   # def drawFLANNMatches(self):
   #     # add "flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS" if you dont wont points not used
   #     matchesMask = [[0,0] for i in range(len(self.matches))]
   #     # ratio test as per Lowe's paper
   #     for i,(m,n) in enumerate(self.matches):
   #         if m.distance < 0.7*n.distance:
   #             matchesMask[i]=[1,0]
   #     draw_params = dict(matchesMask = matchesMask,
   #                         flags = cv.DrawMatchesFlags_DEFAULT)
   #     # cv.drawMatchesKnn expects list of lists as matches.
   #     self.output_img = cv.drawMatchesKnn(self.gray_temp_img,self.keypts_1,self.gray_test_img,self.keypts_2,self.matches,None,**draw_params)
   #     self.output_img = cv.resize(self.output_img, (1280,720))
   #     cv.imshow('Matches', self.output_img)
   #     cv.waitKey(0)