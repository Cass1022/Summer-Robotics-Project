import cv2 as cv


vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()

    # convert color frames to B&W
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    blurredFrame = cv.blur(grayFrame, (3,3))
    (thresh, blurredFrame) = cv.threshold(blurredFrame, 127, 255, cv.THRESH_BINARY)

    detection = cv.Canny(blurredFrame, 70, 135)

    cv.imshow('gray frame', grayFrame)
    cv.imshow('blurred frame', blurredFrame)
    cv.imshow('canny', detection)

    # press 'esc' key to destroy panels
    if cv.waitKey(1) == 27:
        break

vid.release()
cv.destroyAllWindows()

