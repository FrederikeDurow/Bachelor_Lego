import cv2
import numpy as np
import csv

class ConnectedComponents ():
	
	img = None
	output_img = None

	output = None
	mask = None
	componentMask = None

	def __init__(self, low_width, max_width, low_height, max_height, low_area, max_area):
		self.low_Width = low_width
		self.max_Width = max_width
		self.low_Height = low_height
		self.max_Height  = max_height
		self.low_Area = low_area
		self.max_Area = max_area

	def applyConnectedComponents(self,image, connectivity = 8):
		self.img = image

		gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		# Switch between THRESH_BINARY and THRESH_BINARY_INV
		thresh_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

		# 4 checks for (top, left, right, botton) 8 also checks for diagonals
		connectivity = connectivity

		# The last value determine the algorithm (0 SAUF algorithm, 1 BBDT algorithm)
		self.output = cv2.connectedComponentsWithStatsWithAlgorithm(thresh_img, connectivity, cv2.CV_32S,1)
		(numLabels, labels, stats, centroids) = self.output

		self.output_img = image.copy()

		self.mask = np.zeros(gray_img.shape, dtype="uint8")

		for i in range(0, numLabels):
			# print a status message update for the current connected
			# component
			# extract the connected component statistics and centroid for
			# the current label
			x = stats[i, cv2.CC_STAT_LEFT]
			y = stats[i, cv2.CC_STAT_TOP]
			w = stats[i, cv2.CC_STAT_WIDTH]
			h = stats[i, cv2.CC_STAT_HEIGHT]
			area = stats[i, cv2.CC_STAT_AREA]
			(cX, cY) = centroids[i]

			# TUNNED FOR OURS (SHOULD LIMINATE NOISE)
			keepWidth = w > self.low_Width and w < self.max_Width
			keepHeight = h > self.low_Height and h < self.max_Height
			keepArea = area > self.low_Area and area < self.max_Area

			# ensure the connected component we are examining passes all
			# three tests
			if all((keepWidth, keepHeight, keepArea)):
				# construct a mask for the current connected component and
				# then take the bitwise OR with the mask
				print("[INFO] keeping connected component '{}'".format(i))
				self.componentMask = (labels == i).astype("uint8") * 255
				self.mask = cv2.bitwise_or(self.mask, self.componentMask)
				cv2.rectangle(self.output_img, (x, y), (x + w, y + h), (0, 255, 0), 1)
				cv2.circle(self.output_img, (int(cX), int(cY)), 2, (0, 0, 255), -1)

	def drawComponents(self):
		cv2.imshow("Output", self.output_img)
		cv2.imshow("Connected Component", self.componentMask)
		cv2.imshow("Image", self.img)
		cv2.imshow("Mask", self.mask)
		cv2.waitKey(0)

img = cv2.imread('soccer.jpg')

scale_percent = 18 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

test = ConnectedComponents(1,1000,1,1000,1,1000)
test.applyConnectedComponents(resized)
test.drawComponents()




### BELOW CODE WORKS JUST NOT A CLASS
#image = cv2.imread("soccer.jpg")
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
## Switch between THRESH_BINARY and THRESH_BINARY_INV
#thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
#
#cv2.imshow("thresh", thresh)
#
## 4 checks for (top, left, right, botton) 8 also checks for diagonals
#connectivity = 8
#
## The last value determine the algorithm (0 SAUF algorithm, 1 BBDT algorithm)
#output = cv2.connectedComponentsWithStatsWithAlgorithm(thresh, connectivity, cv2.CV_32S,1)
#(numLabels, labels, stats, centroids) = output
#output_img = image.copy()
#
#mask = np.zeros(gray.shape, dtype="uint8")
#
## over the first label (as label zero is the background)
#for i in range(0, numLabels):
#	# print a status message update for the current connected
#	# component
#	# extract the connected component statistics and centroid for
#	# the current label
#	x = stats[i, cv2.CC_STAT_LEFT]
#	y = stats[i, cv2.CC_STAT_TOP]
#	w = stats[i, cv2.CC_STAT_WIDTH]
#	h = stats[i, cv2.CC_STAT_HEIGHT]
#	area = stats[i, cv2.CC_STAT_AREA]
#	(cX, cY) = centroids[i]
#
#	# TUNNED FOR OURS (SHOULD LIMINATE NOISE)
#	keepWidth = w > 1 and w < 10000
#	keepHeight = h > 1 and h < 10000
#	keepArea = area > 1 and area < 10000
#
#	# ensure the connected component we are examining passes all
#	# three tests
#	if all((keepWidth, keepHeight, keepArea)):
#		# construct a mask for the current connected component and
#		# then take the bitwise OR with the mask
#		print("[INFO] keeping connected component '{}'".format(i))
#		componentMask = (labels == i).astype("uint8") * 255
#		mask = cv2.bitwise_or(mask, componentMask)
#		cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 1)
#		cv2.circle(output_img, (int(cX), int(cY)), 2, (0, 0, 255), -1)
#
## show our output image and connected component mask
#cv2.imshow("Output", output_img)
#cv2.imshow("Connected Component", componentMask)
#cv2.imshow("Image", image)
#cv2.imshow("Mask", mask)
#cv2.waitKey(0)