from PIL import Image
import numpy as np

import os


img = Image.open("image.bmp")

width = img.size[0] 
height = img.size[1] 
for i in range(0,width):
    for j in range(0,height):

        data = img.getpixel((i,j))

        if (data[0]==0 and data[1]==255 and data[2]==0):
            img.putpixel((i,j),(255, 0, 0))

        elif (data[0]==255 and data[1]==0 and data[2]==0):
            img.putpixel((i,j),(0, 255, 0))

img.save("image_modified.bmp")

os.system("steghide extract -sf image_modified.bmp -p '' ")

f = open("flag.txt", "r")
print(f.read())