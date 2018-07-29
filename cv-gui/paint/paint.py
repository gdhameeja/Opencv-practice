import cv2
import numpy as np

class Canvas:

    def __init__(self, name, img, brush):
        self.name = name
        self.window = cv2.namedWindow(name)
        self.img = img
        self.set_callback()
                

    def display(self):
        cv2.imshow(self.name, self.img)


    def callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            brush.draw(new_canvas.img, x, y)
            brush.drawing = True

        elif event == cv2.EVENT_MOUSEMOVE:
            if brush.drawing:
                brush.draw(new_canvas.img, x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            brush.drawing = False
 
        
    def set_callback(self):
        cv2.setMouseCallback(self.name, self.callback)

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
new_canvas.brush = brush
brush.canvas = new_canvas


while True:
    new_canvas.display()
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()

