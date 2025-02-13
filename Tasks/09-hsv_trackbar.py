import cv2
import numpy as np

max_count = 100

img = cv2.imread("img/peppers.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV
                   )
cv2.imshow("original", img)
cv2.namedWindow("Slider", cv2.WINDOW_AUTOSIZE)

masked_img = img.copy()

def noise(*args):
    lh = cv2.getTrackbarPos("lowerH", "Slider")
    hh = cv2.getTrackbarPos("higherH", "Slider")
    ls = cv2.getTrackbarPos("lowerS", "Slider")
    hs = cv2.getTrackbarPos("higherS", "Slider")
    lv = cv2.getTrackbarPos("lowerV", "Slider")
    hv = cv2.getTrackbarPos("higherV", "Slider")
    masked_img = add_mask(img, lh, hh, ls, hs, lv, hv)
    cv2.imshow("output", masked_img)

def add_mask(src, c, d, e, f, g, h):
   
    output = np.copy(src)

    lower_bound = np.array([c, e, g])
    upper_bound = np.array([d, f, h])

    output = cv2.inRange(src,lower_bound,upper_bound)

    return output


cv2.createTrackbar("lowerH", "Slider", 0, 255, noise)
cv2.createTrackbar("higherH", "Slider", 0, 255, noise)
cv2.createTrackbar("lowerS", "Slider", 0, 255, noise)
cv2.createTrackbar("higherS", "Slider", 0, 255, noise)
cv2.createTrackbar("lowerV", "Slider", 0, 255, noise)
cv2.createTrackbar("higherV", "Slider", 0, 255, noise)




while True:
    # masked_img = add_mask(img)
    
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # If the ESC key is pressed, break the loop
        break


cv2.destroyAllWindows()
