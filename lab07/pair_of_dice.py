from die import Die

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" PairOfDice class imports Die class and roll two dies."""


class PairOfDice:

    def __init__(self):
        self.a_dice_1 = Die()
        self.a_dice_2 = Die()

    def roll_dice(self):
        self.a_dice_1.roll()
        self.a_dice_2.roll()

    def current_value(self):
        self.roll_dice()
        # Get the sum of two dies.
        self.sum = self.a_dice_1.current_value + self.a_dice_2.current_value
