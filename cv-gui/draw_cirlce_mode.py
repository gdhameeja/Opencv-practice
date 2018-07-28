import cv2
import numpy as np

mode = True
drawing = False
ix, iy = -1, -1

def callback(event, x, y, flags, param):
    global mode, drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (ix, iy), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (ix, iy), 5, (0, 0, 255), -1)     


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('Paint')
cv2.setMouseCallback('Paint', callback)

while True:
    cv2.imshow('Paint', img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break
    elif key == ord('m'):
        mode = not mode

cv2.destroyAllWindows()
            
