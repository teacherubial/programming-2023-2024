# Colour Helper
# Functions that help wither colours


def is_light(pixel: tuple) -> bool:
    """Returns True if the pixel is a "light" pixel

    Params:
        pixel - 3-tuple of values r, g, b

    Returns:
        True if the pixel is a light pixel
        False if a dark pixel
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = (red + green + blue) / 3

    if average >= 128:
        return True
    else:
        return False


def pixel_to_grayscale(pixel: tuple) -> tuple:
    """Return a gray version of the given pixel"""
    red, green, blue = pixel

    gray = int(red * 0.3 + green * 0.59 + blue * 0.11)

    return (gray, gray, gray)


def pixel_to_random_effect(pixel: tuple) -> tuple:
    """Return a random pixel"""
    red, green, blue = pixel

    red += 30
    green += 50
    blue -= 10

    if red > 255:
        red = 255
    if green > 255:
        green = 255
    if blue < 0:
        blue = 0

    return (red, green, blue)
