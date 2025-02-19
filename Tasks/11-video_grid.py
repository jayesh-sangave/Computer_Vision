import cv2
import numpy as np

vid = cv2.VideoCapture(2)

if not vid.isOpened():
    print("Cannot Open Camera")
    exit()

while True:
    ret, frame = vid.read()
    
    if not ret:
        print("Errorrrr")
        break
    
    flip = cv2.flip(frame, -1)
    avg_blur = cv2.blur(frame,(9,9))
    gaussian_blur = cv2.GaussianBlur(frame, (9,9),0)
    median_blur = cv2.medianBlur(frame, 11)
    bilateral_blur = cv2.bilateralFilter(frame, 9, 200,200)

    row0 = np.hstack((frame, flip, median_blur))
    row1 = np.hstack((avg_blur, gaussian_blur, bilateral_blur))

    grid = np.vstack((row0, row1))

    cv2.imshow("grid", grid)

     # Exit the loop when the ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

vid.release()
cv2.destroyAllWindows()