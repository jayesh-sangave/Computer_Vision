import cv2
import numpy as np

img = cv2.imread("img/jetplane.tif", cv2.IMREAD_GRAYSCALE)

kernel_hpf = np.array([[-1, -1, -1],
                       [-1,  8, -1],
                       [-1, -1, -1],]) 

kernel_lpf = np.array([[1, 1, 1],
                       [1, 1, 1],
                       [1, 1, 1],]) /9 

hpf_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_hpf)
lpf_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_lpf)

cv2.imshow("img", img)
cv2.imshow("HPF", hpf_img)
cv2.imshow("LPF", lpf_img)


cv2.waitKey(0)
cv2.destroyAllWindows()

