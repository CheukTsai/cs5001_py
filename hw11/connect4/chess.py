""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Chess:
    """ To draw a single chess """

    def __init__(self, x, y, color, player):
        self.x = x
        self.y = y
        self.c = color
        self.radians = 90
        self.player = player

    def draw_me(self):
        """ To draw chess based on its x, y and color"""
        fill(self.c)
        noStroke()
        circle(self.x, self.y, self.radians)
