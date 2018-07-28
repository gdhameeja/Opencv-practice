from PIL import Image
from pylab import *

# read the image as np array

img = array(Image.open('download.jpg'))

imshow(img)

x = ginput(3)

print("you clicked : ", x)
show()
