# Jelly Bean Colour Counter
# Author: Ubial
# 9 January 2024

# Version 0.1
#  - Count red pixels/beans
#  - Report on the percentage of all red beans
# Version 0.2
#  - Count green pixels/beans
#  - Report on the %age of all green beans

from PIL import Image

import colour_helper

RED_PIXEL = (160, 0, 0)
GREEN_PIXEL = (0, 160, 0)

jelly_bean_img = Image.open("./Images/Jelly Beans.jpg")

red_pixels = []
green_pixels = []

# Visit every pixel in the image
for y in range(jelly_bean_img.height):
    for x in range(jelly_bean_img.width):
        # Get the pixel information
        current_pixel = jelly_bean_img.getpixel((x, y))

        # Detect the current pixel's colour
        if colour_helper.pixel_to_name(current_pixel) == "red":
            red_pixels.append((x, y))
        elif colour_helper.pixel_to_name(current_pixel) == "jelly bean green":
            green_pixels.append((x, y))

# Create a map of all red pixels "found"
# Create a new image that stores the map
#   - the new image should be the same size as original
orig_image_width = jelly_bean_img.width
orig_image_height = jelly_bean_img.height

green_pixel_map = Image.new("RGB", (orig_image_width, orig_image_height))

# For every pixel location in the red_pixels list
# Place a red pixel at that location
for pixel_loc in green_pixels:
    green_pixel_map.putpixel(pixel_loc, GREEN_PIXEL)

# Save the image
green_pixel_map.save("./Images/green_pixel_map.jpg")
green_pixel_map.close()

# Count all the locations of red pixels
red_pixel_count = len(red_pixels)
green_pixel_count = len(green_pixels)
total_pixels = jelly_bean_img.width * jelly_bean_img.height

# Divide by the total pixels in the image
red_pixel_percentage = red_pixel_count / total_pixels * 100
green_pixel_percentage = green_pixel_count / total_pixels * 100

# Generate the report
print(f"Red Jelly Beans: {round(red_pixel_percentage, 2)}%")
print(f"Green Jelly Beans: {round(green_pixel_percentage, 2)}%")

jelly_bean_img.close()
