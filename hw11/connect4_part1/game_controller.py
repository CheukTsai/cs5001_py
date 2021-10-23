from chess import Chess
from board import Board

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class GameController:
    def __init__(self, w, h):
        self.UNIT = 100
        self.HALF_UNIT = 50
        self.COLOR_RED = color(255, 0, 0)
        self.COLOR_YELLOW = color(255, 255, 0)

        self.board = Board(w, h)

        self.w = w
        self.h = h

        self.chess_y = 50
        self.chess_y_vel = 10
        self.release_y = 0
        self.column = 0
        self.row = 0

        self.intact = False
        self.mouse_press = False
        self.player_1 = True
        self.release = True
        self.dropping = False

        self.chesses = []
        self.new_chess = None

    def initialize(self):
        for i in range(self.w / self.UNIT):
            x = []
            self.chesses.append(x)
            for j in range(self.h / self.UNIT - 1):
                x.append(None)

    def update(self):
        if self.check_game_end():
            self.game_over()
        if self.intact and self.check_mouse_area():
            self.hold_and_drop()

        for columns in self.chesses:
            for chess in columns:
                if(chess is not None):
                    chess.draw_me()

        self.board.draw_me()

    def hold_and_drop(self):
        if self.mouse_press and not self.dropping:
            self.column = min(len(self.chesses), mouseX//self.UNIT)
            chess_x = self.column*self.UNIT+self.HALF_UNIT
            self.chess_y = self.HALF_UNIT

        else:
            chess_x = self.column*self.UNIT+self.HALF_UNIT
            self.row = self.check_release_spot(self.column)
            self.release_y = (self.row+1)*self.UNIT + self.HALF_UNIT
            if self.chess_y < self.release_y:
                self.dropping = True
                self.chess_y += self.chess_y_vel

        if not self.check_column_full(self.column):
            new_chess = Chess(chess_x, self.chess_y, self.chess_color())
            new_chess.draw_me()

            if self.chess_y == self.release_y and \
                    self.chess_y > self.HALF_UNIT:
                self.chesses[self.column][self.row] = new_chess
                self.change_player()
                self.intact = False
                self.dropping = False
                self.column = 0

    def chess_color(self):
        if self.player_1:
            chess_color = self.COLOR_RED
        else:
            chess_color = self.COLOR_YELLOW
        return chess_color

    def change_player(self):
        if self.player_1:
            self.player_1 = False
        else:
            self.player_1 = True

    def check_release_spot(self, column):
        for i in range(len(self.chesses[column])):
            if(self.chesses[column][i] is not None):
                return i-1
        return len(self.chesses[column])-1

    def check_game_end(self):
        for column in self.chesses:
            for spot in column:
                if spot is None:
                    return False
        return True

    def check_column_full(self, column):
        for spot in self.chesses[column]:
            if spot is None:
                return False
        return True

    def check_mouse_area(self):
        X_MIN = 0
        X_MAX = self.w
        Y_MIN = 0
        Y_MAX = self.UNIT
        if mouseX >= X_MIN and mouseX <= X_MAX and \
                mouseY >= Y_MIN and mouseY <= Y_MAX:
            return True
        else:
            return False

    def game_over(self):
        TEXT_COLOR = 0
        TEXT_SIZE = 30

        TEXT_X = 10
        TEXT_Y = 50

        fill(TEXT_COLOR)
        textSize(TEXT_SIZE)
        text("GAME OVER", TEXT_X, TEXT_Y)
