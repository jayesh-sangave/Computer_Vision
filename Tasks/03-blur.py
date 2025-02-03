import cv2
import numpy as np

img = cv2.imread("img/jetplane.tif")

avg_blur = cv2.blur(img,(3,3))
gaussian_blur = cv2.GaussianBlur(img, (3,3), 0)
median_blur = cv2.medianBlur(img, 3)
bilateral_blur = cv2.bilateralFilter(img, 9, 90,90)


cv2.imshow("img", img)
cv2.imshow("avg_blur", avg_blur)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)
cv2.imshow("Bilateral Blur", bilateral_blur)


cv2.waitKey(0)
cv2.destroyAllWindows()

