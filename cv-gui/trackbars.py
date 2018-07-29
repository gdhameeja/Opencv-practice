import cv2
import numpy as np

def empty_callback(x):
    pass


# Create a black image and a window
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('Trackbar')

# create trackbars for color change

# trackbar name, window_name, default val, max val, callback
cv2.createTrackbar('R', 'Trackbar', 0, 255, empty_callback) 
cv2.createTrackbar('G', 'Trackbar', 0, 255, empty_callback)
cv2.createTrackbar('B', 'Trackbar', 0, 255, empty_callback)

# create ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'Trackbar', 0, 1, empty_callback)

while True:
    cv2.imshow('Trackbar', img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    # get the current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'Trackbar')
    g = cv2.getTrackbarPos('G', 'Trackbar')
    b = cv2.getTrackbarPos('B', 'Trackbar')
    s = cv2.getTrackbarPos(switch, 'Trackbar')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv2.destroyAllWindows()
