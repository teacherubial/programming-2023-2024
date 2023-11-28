# Functions and Turtle
# Author: Ubial
# 28 November 2023

import turtle

alfred_river_wilson = turtle.Turtle()
alfred_river_wilson.color("lightgreen")
alfred_river_wilson.shape("turtle")


def squared(num: float) -> float:
    """Returns the given number squared"""
    return num**2


def draw_square(side_length: float) -> None:
    for _ in range(4):
        alfred_river_wilson.forward(side_length)
        alfred_river_wilson.left(90)


alfred_river_wilson.speed(0)

# Create a squares that get bigger and bigger
for i in range(50):
    draw_square(squared(i))

turtle.done()
