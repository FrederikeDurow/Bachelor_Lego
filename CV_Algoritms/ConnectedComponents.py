import cv2
import numpy as np

image = cv2.imread("soccer.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Switch between THRESH_BINARY and THRESH_BINARY_INV
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cv2.imshow("thresh", thresh)

# 4 checks for (top, left, right, botton) 8 also checks for diagonals
connectivity = 8

# The last value determine the algorithm (0 SAUF algorithm, 1 BBDT algorithm)
output = cv2.connectedComponentsWithStatsWithAlgorithm(thresh, connectivity, cv2.CV_32S,1)
(numLabels, labels, stats, centroids) = output
output_img = image.copy()

mask = np.zeros(gray.shape, dtype="uint8")

# over the first label (as label zero is the background)
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
	keepWidth = w > 1 and w < 10000
	keepHeight = h > 1 and h < 10000
	keepArea = area > 1 and area < 10000

	# ensure the connected component we are examining passes all
	# three tests
	if all((keepWidth, keepHeight, keepArea)):
		# construct a mask for the current connected component and
		# then take the bitwise OR with the mask
		print("[INFO] keeping connected component '{}'".format(i))
		componentMask = (labels == i).astype("uint8") * 255
		mask = cv2.bitwise_or(mask, componentMask)
		cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 1)
		cv2.circle(output_img, (int(cX), int(cY)), 2, (0, 0, 255), -1)

# show our output image and connected component mask
cv2.imshow("Output", output_img)
cv2.imshow("Connected Component", componentMask)
cv2.imshow("Image", image)
cv2.imshow("Connected Component", mask)
cv2.waitKey(0)