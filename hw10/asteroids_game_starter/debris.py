import random
from flying_object import FlyingObject


""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Debris(FlyingObject):
    """A single piece of spaceship debris"""

    def __init__(self, SPACE, rot,
                 endpoint1, endpoint2,
                 x, y, x_vel, y_vel,
                 radius, fadeout):
        self.SPACE = SPACE
        self.radius = radius
        self.rotation = rot
        self.endpoint1 = endpoint1
        self.endpoint2 = endpoint2
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.rot_vel = self.random_rot_vel()
        self.lifespan = fadeout
        self.fadeout = self.lifespan

    def draw_me(self):
        STROKE_WEIGHT = 3
        # Fade out stroke brightness
        if self.fadeout > 0:
            self.fadeout -= 1
            strokeWeight(STROKE_WEIGHT)
            stroke(
                0,
                (self.fadeout/self.lifespan),
                (self.fadeout/self.lifespan)
            )
            line(*(self.endpoint1 + self.endpoint2))

    def random_rot_vel(self):
        # Isolate this random generator in its
        # own function.
        RANDOM_PERIOD = 2
        return (random.random() * RANDOM_PERIOD) - 0.5
