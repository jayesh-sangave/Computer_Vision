import cv2
import numpy as np

img = cv2.imread("img/MTT.png")
img = cv2.resize(img, (300,300))

img_bw = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(img.copy(), kernel, 3)
dilation = cv2.dilate(img.copy(), kernel, 3)


mask = cv2.inRange(img_bw, 0, 150)
erosion2 = cv2.erode(mask.copy(), kernel, 3)
dilation2 = cv2.dilate(mask.copy(), kernel, 3)


output_img = cv2.bitwise_and(img, img, mask = mask)
erosion3 = cv2.erode(output_img.copy(), kernel, 3)
dilation3 = cv2.dilate(output_img.copy(), kernel, 3)

row1 = np.hstack((img, erosion, dilation))
# row2 = np.hstack((mask, erosion2, dilation2))
row3 = np.hstack((output_img, erosion3, dilation3))

grid = np.vstack((row1, row3))

cv2.imshow("IMG", mask)
cv2.imshow("IMG2", grid)


cv2.waitKey(0)
cv2.destroyAllWindows()

