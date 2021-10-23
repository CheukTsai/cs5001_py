""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Board:
    """ To draw board """

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.UNIT = 100

    def draw_me(self):
        """ To draw board based on the width and height """

        STROKE_WEIGHT = 20.0

        for i in range(0, self.w+1):
            if i % self.UNIT == 0:
                stroke(0, 0, 255)
                strokeWeight(STROKE_WEIGHT)
                line(i, self.UNIT, i, self.h)

        for i in range(self.UNIT, self.h+1):
            if i % self.UNIT == 0:
                stroke(0, 0, 255)
                strokeWeight(STROKE_WEIGHT)
                line(0, i, self.w, i)
