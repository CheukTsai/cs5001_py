from board import Board
from game_controller import GameController

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

SPACE = {"width": 200, "height": 300}
game_controller = GameController(SPACE["width"], SPACE["height"])
game_controller.initialize()


def setup():
    size(SPACE["width"], SPACE["height"])
    colorMode(RGB, 1)


def draw():
    global x
    background(1)
    game_controller.update()


def mousePressed():
    game_controller.intact = True
    game_controller.mouse_press = True


def mouseReleased():
    game_controller.mouse_press = False
