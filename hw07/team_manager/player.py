""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class Player:
    """A class representing a dodgeball player"""
    # TODO: Write a constructor (__init__() method) that
    # will take the necessary values, set them to
    # the player object's attributes, and create the
    # new instance of player. Like all methods, its first
    # parameter must be `self`. The remaining parameters should
    # receive whatever pieces of data are relevant to creating
    # a new Player object.

    def __init__(self, name, number, position):
        # Three necessary values
        self.name = name
        self.number = number
        self.position = position

    def __str__(self):
        # Override class player with certain format
        return f"{self.number}\t{self.name}\t{self.position}"

    pass
