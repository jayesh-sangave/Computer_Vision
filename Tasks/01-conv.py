import cv2
import numpy as np

img = cv2.imread("img/jetplane.tif", cv2.IMREAD_GRAYSCALE)

kernel_arr = np.array([[0, 0, 0],
                       [0, 1, 0],
                       [0, 0, 0],]) # Identity Matrix

output_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel_arr)

cv2.imshow("img", img)
cv2.imshow("Output", output_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

