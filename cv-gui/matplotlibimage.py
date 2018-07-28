import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('download.jpg', cv.IMREAD_GRAYSCALE)

plt.imshow(img, cmap='gray', interpolation='bicubic')

plt.show()
