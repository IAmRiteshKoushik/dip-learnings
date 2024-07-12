# 1. High resoulution images and frames ahve a lot of information in it and 
# displaying it takes up a lot of processing power. It is best to rescale and 
# resize it so that we can get rid of some information.

# 2. Rescaling a video means height and width
# 3. Generally, you downscale (reduce size) 

import cv2 as cv

# img = cv.imread("Photos/cat_large2.jpg")
# cv.imshow("Cat", img)

def rescaleFrame(frame, scale = 0.75):
    # Height and width ar integers and after multiplication they become 
    # floating point numbers. In order to fix that, we need to typecase again 
    # in int()
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    # resizes a video to a particular dimension
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()

    # Intermediate function used to change the size of the frame
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()

