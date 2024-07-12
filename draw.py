import cv2 as cv
import numpy as np

# A 500x500 matrix is created where each cell itself is an array of 3 values
# These 3 values are going to represent [RGB]
# uint8 can hold 256 (2^8) values --

# 1. 3 of these can hold 2^24 values
# 2. 6 character hexadecimal can hold 16^6 = (2^4)^6 = 2 ^ 24
blank = np.zeros((500, 500, 3), dtype="uint8")
print(blank)
cv.imshow("Blank", blank) # returns a black iimage

# Point the image a certain color by setting all the pixels to RGB::0,255,0
blank[:] = 0, 255, 0
cv.imshow("Green", blank)

cv.waitKey(0)
