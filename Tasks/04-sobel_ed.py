import cv2
import numpy as np

img = cv2.imread("img/baboon.png")

sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, 3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, 3)
sobel_combined = cv2.magnitude(sobel_x, sobel_y)    
sobel_display = cv2.convertScaleAbs(sobel_combined)

cv2.imshow("img", img)
cv2.imshow("Sobel", sobel_display)


cv2.waitKey(0)
cv2.destroyAllWindows()

