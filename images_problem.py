# Images Problem
# Author: Ubial
# 18 December 2023

from PIL import Image

import colour_helper

# Test?
light_pixel = (255, 255, 255)
light_gray = (128, 128, 128)
darker_gray = (100, 128, 128)
reddish_pixel = (255, 100, 24)
dark_gray = (127, 127, 127)
dark_pixel = (0, 0, 0)

print(colour_helper.is_light(light_pixel))  # True
print(colour_helper.is_light(light_gray))  # True
print(colour_helper.is_light(reddish_pixel))  # False
print(colour_helper.is_light(dark_gray))  # False
print(colour_helper.is_light(dark_pixel))  # False


def binarize() -> None:
    """Binarizes an image"""

    # Open the image
    with Image.open("./Images/catto.png") as im:
        image_height = im.height
        image_width = im.width

        # starting at the top and working our way down
        # visit the pixels from left to right
        for y in range(image_height):
            for x in range(image_width):
                pixel = im.getpixel((x, y))

                # if the pixel is light
                if colour_helper.is_light(pixel):
                    im.putpixel((x, y), light_pixel)
                else:
                    im.putpixel((x, y), dark_pixel)

        # After visiting every pixel, save the image
        im.save("./Images/binarized.jpg")


def picture_to_grayscale(filename: str) -> None:
    """Convert a given picture to grayscale"""

    # Open up the image
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                # Take that pixel and convert it to gray
                gray_pixel = colour_helper.pixel_to_grayscale(pixel)

                im.putpixel((x, y), gray_pixel)

        # Save the image
        im.save("./Images/grayscale.jpg")


def random_picture_effect(filename: str) -> None:
    """Convert a given picture to something random"""

    # Open up the image
    with Image.open(f"./Images/{filename}") as im:
        # Visit every pixel
        for y in range(im.height):
            for x in range(im.width):
                pixel = im.getpixel((x, y))

                # Take that pixel and randomize it
                random_pixel = colour_helper.pixel_to_random_effect(pixel)
                im.putpixel((x, y), random_pixel)

        # Save the image
        im.save("./Images/random.jpg")


# picture_to_grayscale("best_pizza.jpg")
random_picture_effect("best_pizza.jpg")
