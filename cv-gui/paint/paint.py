import cv2
import numpy as np

class Canvas:

    def __init__(self, name, img, brush):
        self.name = name
        self.window = cv2.namedWindow(name)
        self.img = img
        self.brush = brush
        self.set_callback()
        self.add_trackbars()
        
    def display(self):
        cv2.imshow(self.name, self.img)
        

    def callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.brush.draw(new_canvas.img, x, y)
            self.brush.drawing = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if self.brush.drawing:
                self.brush.draw(new_canvas.img, x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.brush.drawing = False
 
        
    def set_callback(self):
        cv2.setMouseCallback(self.name, self.callback)

    def empty_callback(self, x):
        pass
    
    def add_trackbars(self):
        cv2.createTrackbar('R', self.name, 0, 255, lambda x: None)
        cv2.createTrackbar('G', self.name, 0, 255, lambda x: None)
        cv2.createTrackbar('B', self.name, 0, 255, lambda x: None)
        
        
class Brush:

    def __init__(self, color):
        self.color = color
        self.drawing = False

    def draw(self, img, x, y):
        cv2.circle(img , (x, y), 3, self.color, -1)
        

img = np.zeros((300, 512, 3), np.uint8)
img[:] = [255, 255, 255]
brush = Brush((255, 0, 0))
new_canvas = Canvas('Image', img, brush)


while True:
    new_canvas.display()
    r = cv2.getTrackbarPos('R', new_canvas.name)
    g = cv2.getTrackbarPos('G', new_canvas.name)
    b = cv2.getTrackbarPos('B', new_canvas.name)

    brush.color = (r, g, b)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

