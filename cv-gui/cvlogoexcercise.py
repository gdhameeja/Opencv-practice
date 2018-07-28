import cv2
import numpy as np

color = None
mode = True # if true create triangle, else create a circle
# callback for the mouse click
def callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x, y), 5, color, -1)
                


cv2.namedWindow('OpenCVLogo')
cv2.setMouseCallback('OpenCVLogo', callback)
img = np.zeros((512, 512, 3), np.uint8)

while True:
    cv2.imshow('OpenCVLogo', img)
    global color
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('m'):
        mode = not mode
    elif key == ord('b'):
        color = (255, 0, 0)
    elif key == ord('r'):
        color = (0, 0, 255)
    elif key == ord('g'):
        color = (0, 255, 0)
    elif key == ord('w'):
        color = (255, 255, 255)
                
cv2.destroyAllWindows()
    
