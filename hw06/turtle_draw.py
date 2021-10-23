import math
import turtle as t

""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


""" This program aims at creating a specific graphic
with turtle graphics module. """

""" Two reminders:
1. Default colors (yellow, red or blue) in Windows
is different from the needed color. Thus, I used PhotoShop
to figure out the specific color code for each color;

2. Even though using the same methods, Windows cannot automatically show
the pentagon in blue. Thus, need to draw it specifically;

3. Some warnings pop out about turtle module, but never affect the
final outputs. Seek for help from TAs, all replied that it would be fine."""


# Basic constants for multiplication
DOUBLE_VALUE = 2
HALF_VALUE = 1/2

# Some parameters of angles
FLAT_ANGLE = 180
ANGLE_OF_STAR = 36
ANGLE_OF_ADJUSTMENT_DRAW_STAR_BEGINNING = 72

SIN_18 = math.sin(math.radians(
    HALF_VALUE*ANGLE_OF_STAR))
COS_18 = math.cos(math.radians(
    HALF_VALUE*ANGLE_OF_STAR))
COS_72 = SIN_18

# Constants to draw star
NUMBER_OF_SEGMENTS_OF_STAR = 5
ANGLE_OF_ADJUSTMENT_DRAW_STAR_PROGRESS = FLAT_ANGLE - ANGLE_OF_STAR
SEGMENT_OF_STAR = 500


# Constant to draw circle
RADIAN_OF_CIRCLE = (HALF_VALUE*SEGMENT_OF_STAR)/COS_18

# Constant to draw pentagon in middle
NUMBER_OF_SEGMENTS_OF_PENTAGON = 5
ANGLE_OF_ADJUSTMENT_DRAW_PENTAGON = 72
DISTANCE_TO_SET_PEN_DRAW_PENTAGON = SEGMENT_OF_STAR/(
    DOUBLE_VALUE*(1+COS_72))
SEGMENT_OF_PENTAGON = SEGMENT_OF_STAR/(1+SIN_18)*SIN_18

# Color codes
DARK_BLUE = "#003fff"
LIGHT_BLUE = "#00ffff"
RED = "#ff3700"
YELLOW = "#ffff00"


""" distance = 2*y*math.cos(math.pi*(18/180))
angle = 1
a = math.cos(math.pi*(72/180))
x = 2*(1+a) """


def draw_circle():
    # Preparation
    t.penup()
    t.setposition(0, -1*RADIAN_OF_CIRCLE)
    t.pendown()

    # Directly draw and fill the circle
    t.color(DARK_BLUE, LIGHT_BLUE)
    t.begin_fill()
    t.circle(RADIAN_OF_CIRCLE)
    t.end_fill()


def draw_star():
    # Preparation
    t.penup()
    t.setposition(0, RADIAN_OF_CIRCLE)
    t.pendown()

    # Directly draw and fill the star
    t.right(ANGLE_OF_ADJUSTMENT_DRAW_STAR_BEGINNING)
    t.color(RED, YELLOW)
    t.begin_fill()
    for i in range(NUMBER_OF_SEGMENTS_OF_STAR):
        t.forward(SEGMENT_OF_STAR)
        t.right(ANGLE_OF_ADJUSTMENT_DRAW_STAR_PROGRESS)
    t.end_fill()


def draw_pentagon():

    # Preparation: No need to change pen position
    # just move pen forward in same direction
    t.forward(DISTANCE_TO_SET_PEN_DRAW_PENTAGON)

    # Directly draw and fill the pentagon
    t.color(RED, LIGHT_BLUE)
    t.begin_fill()
    for i in range(NUMBER_OF_SEGMENTS_OF_PENTAGON):
        t.forward(SEGMENT_OF_PENTAGON)
        t.right(ANGLE_OF_ADJUSTMENT_DRAW_PENTAGON)
    t.end_fill()


def main():
    # Make pen invisible
    t.hideturtle()

    draw_circle()
    draw_star()
    draw_pentagon()

    # Quit program when user clicks mouse button
    t.exitonclick()


main()
