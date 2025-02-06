import cv2
import numpy as np

img = cv2.imread("img/peppers.png")

def add_noise(src):
    pixel_count = src.size
    output = np.copy(src)

    salt_count = int(pixel_count * 0.1)
    pepper_count = int(pixel_count * 0.1)

    salt_pos = [np.random.randint(0, i-1, salt_count) for i in src.shape]
    output[salt_pos[0], salt_pos[1]] = 255

    pepper_pos = [np.random.randint(0, i-1, pepper_count) for i in src.shape]
    output[pepper_pos[0], pepper_pos[1]] = 0

    return output

img_noise = add_noise(img)

cv2.imshow("original", img)
cv2.imshow("output", output)
    


cv2.waitKey(0)
cv2.destroyAllWindows()

