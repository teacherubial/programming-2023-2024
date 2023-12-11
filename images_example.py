# Images and Python
# Author: Ubial
# 11 December 2023

from PIL import Image

# open up kid green
with Image.open("./Images/kid-green.jpg") as im:
    # grab the pixel in the top left corner
    pixel = im.getpixel((0, 0))
    # print the pixel information
    print(pixel)
