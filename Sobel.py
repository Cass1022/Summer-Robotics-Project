import cv2 as cv


vid = cv.VideoCapture(0)

while True:
    ret, frame = vid.read()

    # convert color frames to B&W
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    (thresh, grayFrame) = cv.threshold(grayFrame, 127, 255, cv.THRESH_BINARY)

    sobel_x = cv.Sobel(grayFrame, cv.CV_64F, 1, 0, ksize = 5)
    sobel_y = cv.Sobel(grayFrame, cv.CV_64F, 0, 1, ksize = 5)
    laplacian = cv.Laplacian(grayFrame, cv.CV_64F)

    # cv.imshow('x', sobel_x)
    # cv.imshow('y', sobel_y)
    cv.imshow('Laplacian', laplacian)

    # cv.imshow('Blurred frame', blurredFrame) # camera display for B&W with convolution
    # cv.imshow('Original frame', frame) # camera display in color
    # cv.imshow('Black and white frame', grayFrame) # camera display in black and white

    # press 'esc' key to destroy panels
    if cv.waitKey(1) == 27:
        break

vid.release()
cv.destroyAllWindows()

