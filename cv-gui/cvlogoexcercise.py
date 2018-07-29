import cv2
import numpy as np

color = None
triangle_vertices = []
mode = True  # if true create circle, else create a triangle

# callback for the mouse click
def callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if mode:
            global triangle_vertices
            triangle_vertices = []
            cv2.circle(img, (x, y), 50, color, -1)
        else:
            # draw the triangle
            global triangle_vertices
            if len(triangle_vertices) != 3:
                triangle_vertices.append([x, y])
            else:
                print(triangle_vertices)
                pts = np.array(triangle_vertices)
                pts = pts.reshape(3, 1, 2)
                cv2.polylines(img, [pts], True, (255, 255, 255))
                triangle_vertices = []

cv2.namedWindow('OpenCVLogo')
cv2.setMouseCallback('OpenCVLogo', callback)
img = np.zeros((512, 512, 3), np.uint8)

while True:
    cv2.imshow('OpenCVLogo', img)
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



























