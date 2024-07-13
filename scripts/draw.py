import cv2 as cv
import numpy as np

# A 500x500 matrix is created where each cell itself is an array of 3 values
# These 3 values are going to represent [RGB]
# uint8 can hold 256 (2^8) values --

# 1. 3 of these can hold 2^24 values
# 2. 6 character hexadecimal can hold 16^6 = (2^4)^6 = 2 ^ 24
blank = np.zeros((500, 500, 3), dtype="uint8")
# print(blank)
cv.imshow("Blank", blank) # returns a black iimage

# 1. Draw a quadrilateral
# Point the image a certain color by setting all the pixels to RGB::0,255,0
# blank[:] = 0, 255, 0
blank[200:300, 300:400] = 0, 0, 255
cv.imshow("Green", blank)

# 2. Draw a Rectangle
# Alternate ways to do the same
# Params - image, start-coord, end-coord, color(RGB), thickenss
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)

# You can choose to generate the end coordinates fo the diagonal for mapping the 
# entire rectangle through the dimensions of the image as well
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=cv.FILLED)
# cv.FILLED is used to created a solid shape (instead of outlined)
# -1 achieves the same results
cv.imshow('Rectangle', blank)

# 3. Draw a circle
# Params - image-matrix, coordinates for center, radius, color, thickness
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), 
          thickness=-1)
cv.imshow("Circle", blank)

# 4. Draw a line
cv.line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2),
        (255, 255, 255), thickness=3)
cv.imshow("Line", blank)

cv.waitKey(0)
