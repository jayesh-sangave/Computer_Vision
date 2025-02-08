import cv2
import numpy as np

img = cv2.imread("img/MTT.png")
img = cv2.resize(img, (300,300))

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(img.copy(), kernel, 3)
dilation = cv2.dilate(img.copy(), kernel, 3)

row = np.hstack((img,erosion, dilation))

cv2.imshow("IMG", row)

cv2.waitKey(0)
cv2.destroyAllWindows()

