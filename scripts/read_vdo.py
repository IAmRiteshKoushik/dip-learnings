import cv2 as cv 

# Reading Videos - 
# 1. Can capture videos from webCams with args - 0, 1, 2, .. (cameras connected)
# 2. Or provide a string which contains a file path
capture = cv.VideoCapture("Videos/dog.mp4")

# We use a while loop and read the video frame-by-frame
while True:
    # read returns 2 values, the frame and whether the frame was successfully
    # read or not.
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    # Wait for 20 seconds or if the letter D is pressed 
    # As of latest information : Masking is redundant (check it out)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Deallocate memory - avoid memory leaks
# 1. Release the pointer to the file
capture.release()
# 2. Destroy all windows
cv.destroyAllWindows()

# NOTE: You will get an assertion failed error when the video runs out of 
# frames. "isTrue" will become false. Basically, it cannot be read
