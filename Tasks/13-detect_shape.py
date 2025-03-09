import cv2
import numpy as np


img = cv2.imread("img/Polygon.jpg")
img = cv2.resize(img, (300, 300))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(img_gray, 235, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

max_area = 0
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > max_area:
        max_area = area

for cnt in contours:
    area = cv2.contourArea(cnt)
    approx = cv2.approxPolyDP(cnt, 0.1 * cv2.arcLength(cnt, True), True)
    print(approx)
    if area < 0.9 * max_area:
        if len(approx) == 5:
            cv2.drawContours(img, [approx], -1 ,(0,0,255), 2)
        if len(approx) == 3:
            cv2.drawContours(img, [approx], -1 ,(255,0,255), 2)

cv2.imshow("Src", img)   
cv2.imshow("Output", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
