# Metoden her bruger triangular similarity som dens måde at regne det ud på
# Her bruger den en objekt den allerede kender dimensionerne på.
# Derefter laver man noget billede behandling for at udtrække dens countour

# Oplagt vil være at bruge vores "chess picece board" som vi bruger til calibration
# Dertil kan man lave en algoritme som finder nærliggende corners.
# Dette bør kun køre 1 gang inden en test da den 
# Focallength parameteren burde stå i vores kamera parameter fil XML

# import the necessary packages
from imutils import paths
import numpy as np
import imutils
import cv2

# SHOULD BE OF OUR CHESS BOARDIN MM
KNOWN_WIDTH = 11.0

# FROM OUR CAMERA CALIBRATION
focalLength = 1

def find_marker(image):
	# convert the image to grayscale, blur it, and detect edges
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 35, 125)
	# find the contours in the edged image and keep the largest one;
	# we'll assume that this is our piece of paper in the image

    # SHOULD BE OUR OWN
	cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	c = max(cnts, key = cv2.contourArea)


	# compute the bounding box of the of the paper region and return it
	return cv2.minAreaRect(c)

def distance_to_camera(knownWidth, focalLength, pixelWidth):
	# compute and return the distance from the maker to the camera
	return (knownWidth * focalLength) / pixelWidth

def drawDistance(image):
    img = image
    marker = find_marker(img)
    millimeters = distance_to_camera(KNOWN_WIDTH, focalLength, marker)
    cv2.putText(image, "%.2fft" % (millimeters / 12),
		(image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,
		2.0, (0, 255, 0), 3)