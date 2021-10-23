# ControlP5 is a 3rd party library that gives us
# interface controls. We need it for the slider.

# Unable to solve the problem that
# "module level import not at top of file"
# since we have to use the function
# add_library at the very beginning

add_library('controlP5')
from controlP5 import ControlP5
from controlP5 import Slider

# Here we import the Point class definition from
# the other tab of this sketch. That file is
# and ordinary .py file stored in the same
# sketch directory.

from point import Point

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

# For setting up the slider
MIN_DEPTH = 0
MAX_DEPTH = 8

# Coords of starting triangle
TOP_X = 200
TOP_Y = 100
LEFT_X = 50
LEFT_Y = 350
RIGHT_X = 350
RIGHT_Y = 350

startLeft = Point(LEFT_X, LEFT_Y)
startRight = Point(RIGHT_X, RIGHT_Y)
startTop = Point(TOP_X, TOP_Y)

# Controls the recursive depth
depth = 0


# This code is executed only once, at the beginning
# of your sketch. Conceptually, the setup function has
# a similar role to a class's constructor
def setup():
    size(430, 400)
    noStroke()
    setupSlider()


# The draw method is executed repeatedly, coinciding
# with screen refreshes. Anything that needs to be
# redrawn, recalculated, animated, or to respond to
# user interaction will need to be carried out within the
# draw loop.
def draw():
    background(0)

    # Draws the initial white triangle
    fill(255)
    triangle(startLeft.getX(), startLeft.getY(),
             startRight.getX(), startRight.getY(),
             startTop.getX(), startTop.getY())
    sierpinksi(startLeft, startRight, startTop, depth)


# This is a recursive function that draws the Sierpinski triangle
def sierpinksi(bottomLeft, bottomRight, top, recursionDepth):
    if(recursionDepth > 0):

        # First create the 3 points of the
        # new black triangle
        blackLeft = bottomLeft.midPoint(top)
        blackRight = top.midPoint(bottomRight)
        blackBottom = bottomRight.midPoint(bottomLeft)

        # Draw the triangle
        fill(0)
        triangle(blackLeft.getX(), blackLeft.getY(),
                 blackRight.getX(), blackRight.getY(),
                 blackBottom.getX(), blackBottom.getY())

        # In every loop, the recursion depth
        # will decrease by 1
        recursionDepth -= 1

        # Recursion: 3 new white triangle will be created
        # based on the midpoints
        sierpinksi(bottomLeft, blackBottom, blackLeft, recursionDepth)
        sierpinksi(blackBottom, bottomRight, blackRight, recursionDepth)
        sierpinksi(blackLeft, blackRight, top, recursionDepth)

    else:
        return


# The code below sets up the slider and sets a listener callback
# function to respond to the user sliding the slider.
def setupSlider():
    cp5 = ControlP5(this)
    depthSlider = cp5.addSlider("Recursion Depth")\
        .setPosition(20, 20)\
        .setSize(200, 40)\
        .setRange(MIN_DEPTH, MAX_DEPTH)\
        .setNumberOfTickMarks(9)\
        .addListener(listener)


def listener(event):
    global depth
    depth = event.value()
