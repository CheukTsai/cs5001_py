from flying_object import FlyingObject

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Asteroid(FlyingObject):
    """An asteroid"""

    def __init__(self, SPACE, asize='Large',
                 x=100, y=100, x_vel=0.2, y_vel=0.25,
                 rot=0.0, rot_vel=1.0):
        self.SPACE = SPACE
        self.x = x
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rotation = rot
        self.rot_vel = rot_vel
        self.asize = asize
        if self.asize == 'Large':
            self.radius = 65
        if self.asize == 'Med':
            self.radius = 40
        if self.asize == 'Small':
            self.radius = 25

    def draw_me(self):
        STROKE_COLOR = (0.8, 0.8, 0.8)
        STROKE_WEIGHT = 3
        FILL_COLOR = 0

        stroke(*STROKE_COLOR)
        fill(FILL_COLOR)
        strokeWeight(STROKE_WEIGHT)

        beginShape()
        if self.asize == 'Large':
            self.large_shape()

        if self.asize == 'Med':
            self.med_shape()

        if self.asize == 'Small':
            self.small_shape()
        endShape(CLOSE)

    # There's not much to be gained in terms of readability in
    # breaking the numbers below out into constants. For this
    # reason we're  going to isolate them into their own functions
    # as much as possible. We can see that the numbers are
    # coordinates for vertices to draw specific odd shapes.
    def large_shape(self):
        POINT_X_1 = 30
        POINT_X_2 = 50
        POINT_X_3 = 60
        POINT_X_4 = 40

        POINT_Y_1 = 30
        POINT_Y_2 = 50
        POINT_Y_3 = 40
        POINT_Y_4 = 20

        vertex(-POINT_X_1, -POINT_Y_1)  # upper left
        vertex(0, -POINT_Y_2)
        vertex(POINT_X_2, -POINT_Y_3)  # upper right
        vertex(POINT_X_3, 0)
        vertex(POINT_X_1, POINT_Y_2)  # lower right
        vertex(0, POINT_Y_4)
        vertex(-POINT_X_4, POINT_Y_1)  # lower left
        vertex(-POINT_X_2, 0)

    def med_shape(self):
        POINT_X_1 = 30
        POINT_X_2 = 25
        POINT_X_3 = 15
        POINT_X_4 = 10

        POINT_Y_1 = 25
        POINT_Y_2 = 30
        POINT_Y_3 = 20
        POINT_Y_4 = 10

        vertex(-POINT_X_1, -POINT_Y_1)  # upper left
        vertex(0, -POINT_Y_2)
        vertex(POINT_X_1, -POINT_Y_3)  # upper right
        vertex(POINT_X_2, 0)
        vertex(POINT_X_3, POINT_Y_4)  # lower right
        vertex(-POINT_X_4, POINT_Y_3)  # lower left
        vertex(-POINT_X_2, 0)

    def small_shape(self):
        POINT_X_1 = 15
        POINT_X_2 = 18
        POINT_X_3 = 20

        POINT_Y_1 = 20
        POINT_Y_2 = 15
        POINT_Y_3 = 10

        vertex(0, -POINT_Y_1)
        vertex(POINT_X_1, 0)
        vertex(0, POINT_Y_2)
        vertex(-POINT_X_2, POINT_Y_3)  # lower left
        vertex(-POINT_X_3, 0)
