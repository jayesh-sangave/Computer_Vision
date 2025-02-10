import cv2
import numpy as np

max_count = 100

img = cv2.imread("img/peppers.png")
cv2.imshow("original", img)
cv2.namedWindow("Slider", cv2.WINDOW_AUTOSIZE)

noisy_img = img.copy()

def noise(*args):
    global noisy_img
    prob = args[0]/100
    noisy_img = add_noise(img, prob)

def add_noise(src, c):
    pixel_count = src.size
    output = np.copy(src)

    salt_count = int(pixel_count * c)
    pepper_count = int(pixel_count * c)

    salt_pos = [np.random.randint(0, i-1, salt_count) for i in src.shape]
    output[salt_pos[0], salt_pos[1]] = 255

    pepper_pos = [np.random.randint(0, i-1, pepper_count) for i in src.shape]
    output[pepper_pos[0], pepper_pos[1]] = 0

    return output


cv2.createTrackbar("Percentage", "Slider", 1, 100, noise)


while True:
    # noisy_img = add_noise(img)
    cv2.imshow("output", noisy_img)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # If the ESC key is pressed, break the loop
        break
    # cv2.waitKey(0)

cv2.destroyAllWindows()
