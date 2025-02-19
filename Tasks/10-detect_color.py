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

    h, w, _ = frame.shape

    x = w // 2
    y = h // 2

    roi = frame[x:x+1,y:y+1]

    hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    pixel = hsv_roi[0, 0, 0]

    if pixel in range(90, 130):
        cv2.putText(frame, "Blue", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2, cv2.LINE_AA)
        print("Blue")
    elif pixel in range(30, 80):
        cv2.putText(frame, "Green", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2, cv2.LINE_AA)
        print("Green")
    else:
        cv2.putText(frame, "None", (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255), 2, cv2.LINE_AA)

    cv2.circle(frame, (x, y), 5, (0, 255, 0), 2)

    cv2.imshow("Video Stream", frame)

     # Exit the loop when the ESC key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

vid.release()
cv2.destroyAllWindows()