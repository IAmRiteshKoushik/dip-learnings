import cv2 as cv

img = cv.imread("Photos/cat.jpg")
img[200:300, 300:400] = 0, 0, 255
# img[100:600, 200:600] = 0, 0, 255
# cv.imwrite("cat-recreated.png", img[100:600, 200:600])  # saving image to disc
cv.imshow("Cat", img)

cv.waitKey(0)

