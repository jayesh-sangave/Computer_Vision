import cv2
import numpy as np

img = cv2.imread("img/MTT.png", cv2.IMREAD_GRAYSCALE)

kernel = np.ones((10,10), np.uint8)
erosion = cv2.erode(img.copy(), kernel, 10)
dilation = cv2.dilate(img.copy(), kernel, 10)

row = np.hstack((img,erosion, dilation))

cv2.imshow("IMG", row)

cv2.waitKey(0)
cv2.destroyAllWindows()

