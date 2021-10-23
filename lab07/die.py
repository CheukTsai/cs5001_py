import random as r

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Die:
    """ Die class creates a single die with 6 faces."""

    MIN_VALUE = 1
    MAX_VALUE = 6

    def __init__(self):

        self.current_value = r.randint(
            Die.MIN_VALUE, Die.MAX_VALUE)  # Face-up value

    def roll(self):
        self.current_value = r.randint(
            Die.MIN_VALUE, Die.MAX_VALUE)  # Roll the dice
