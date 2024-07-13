import cv2 as cv

# 1 param - path to image; returns -> matrix-like type 
img = cv.imread("Photos/cat_large.jpg")

# 2 params - name of the window, matrix returned from imread()
cv.imshow("Cat", img)

# Allows you to show for a specific period of time
cv.waitKey(0)       # 0 means wait till the next key is pressed
