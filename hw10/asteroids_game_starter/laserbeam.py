from flying_object import FlyingObject

# TODO: Problem 3, Part 1: Laser beam lifespans
#
# Implement laser beam lifespan and whatever
# further logic is needed to ensure that the
# laser beam's remaining lifespan is updated
# with each frame. You may make changes anywhere
""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

# in this class definition.

# Set the lifespan to a default of 100 frames.


class LaserBeam(FlyingObject):
    """A single laser torpedo"""

    def __init__(self, SPACE, x, y, x_vel, y_vel):
        self.LASER_SPEED_FACTOR = 5
        self.SPACE = SPACE
        self.rotation = 0.0

        self.RADIUS_NUM = 2.5
        self.radius = self.RADIUS_NUM

        self.diam = self.radius*2
        self.x_vel = x_vel * self.LASER_SPEED_FACTOR
        self.y_vel = y_vel * self.LASER_SPEED_FACTOR
        self.x = x + x_vel
        self.y = y + y_vel

        self.FADEOUT_FACTOR = 100
        self.lifespan = self.FADEOUT_FACTOR

    def draw_me(self):
        FILL_COLOR = 1
        fill(FILL_COLOR)
        noStroke()
        ellipse(0, 0, self.diam, self.diam)
