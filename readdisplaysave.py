import cv2 as cv

# read the image, as grayscale
img = cv.imread('download.jpg', cv.IMREAD_GRAYSCALE)

# display the read image
cv.imshow('WindowName', img)

# wait for a key to be pressed undefinitely. 
key = cv.waitKey(0)

if key is ord('s'):
    cv.imwrite('graydownload.jpg', img)
    cv.destroyAllWindows()
elif key == 27:
    cv.destroyAllWindows()
