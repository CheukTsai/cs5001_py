from chess import Chess
from board import Board
import time
import math as m
import random
import copy

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class GameController:
    def __init__(self, w, h):
        self.UNIT = 100
        self.HALF_UNIT = 50

        self.board = Board(w, h)

        self.w = w
        self.h = h

        self.score_file = {}
        self.chess_y = 50
        self.chess_y_vel = 25
        self.chess_y_ai = 50
        self.column_ai = 0
        self.release_y = 0
        self.release_y_ai = 0
        self.row_ai = 0
        self.column = None
        self.row = 0

        self.intact = False
        self.mouse_press = False
        self.player_1 = True
        self.release = True
        self.dropping = False
        self.depth = 5
        self.name = None
        self.winner_picked = False

        self.chesses = []
        self.chess_board = []
        self.new_chess = None
        self.player_human = 1
        self.player_ai = 2
        self.col = -1
        self.ai_dropping = False

    def initialize(self):
        """ Initialize the board """
        for i in range(int(self.w / self.UNIT)):
            x = []
            self.chesses.append(x)
            for j in range(int(self.h / self.UNIT) - 1):
                x.append(None)
        # self.chess_board = [
        #     [0 for _ in range(self.row_total)] for _ in range(
        #       self.column_total)]

    def read_the_score(self):
        '''
        Read the name and score, then sort them.
        None -> None
        '''

        f = open("scores.txt", 'r')
        for line in f:
            score_list = line.rstrip().split()
            score = score_list[-1]
            score_list.pop(-1)
            name = ' '.join(score_list)
            self.score_file[name] = int(score)
        f.close()

    def write_the_score(self):
        '''
        Record the name and corresponding score.
        None -> None
        '''
        name = self.user_input('Please enter your name')
        while(name is None or name == ''):
            name = self.user_input('Please enter your name')
        if name in self.score_file.keys():
            self.score_file[name] += 1
        else:
            self.score_file[name] = 1
        player_names = self.top_n_counts()

        f = open("scores.txt", "w")
        for score in player_names:
            s = score[0] + ' ' + str(score[1]) + '\n'
            f.write(s)
        f.close()

    def top_n_counts(self):
        '''
        Sort the self.scores in a descending
        order.
        None -> List
        '''
        return sorted(
            self.score_file.items(),
            key=lambda x: x[1],
            reverse=True)

    def user_input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def update(self):
        '''
        The main update function for the whole drawing part
        '''
        for columns in self.chesses:
            for chess in columns:
                if(chess is not None):
                    chess.draw_me()
        self.board.draw_me()

        if self.check_winner() is not None:
            self.winner_picked = True
            self.win_display(self.check_winner())
            noLoop()
            if self.check_winner():
                self.read_the_score()
                self.write_the_score()
                noLoop()

        elif self.check_game_end():
            self.game_over()
            noLoop()
        else:
            if self.player_1:
                if self.intact:
                    self.hold_and_drop()
            else:
                if self.col == -1:
                    self.col = random.randint(0, int(self.w / self.UNIT)-1)
                    time.sleep(1)
                # if not self.ai_dropping:
                #     self.col, minimax_score = self.minimax(
                #         self.chess_board,
                #       self.depth, -1000000000, 1000000000, True)
                else:
                    self.hold_and_drop_ai(self.col)
            self.board.draw_me()

    def hold_and_drop(self):
        '''
        To act the pressing and droping move for human player
        '''
        if self.mouse_press and not self.dropping and self.check_mouse_area():
            self.column = mouseX//self.UNIT
            chess_x = self.column*self.UNIT+self.HALF_UNIT
            self.chess_y = self.HALF_UNIT

        else:
            chess_x = self.column*self.UNIT+self.HALF_UNIT
            self.row = self.check_release_spot(self.column)
            self.release_y = (self.check_release_spot(
                self.column)+1)*self.UNIT + self.HALF_UNIT
            if self.chess_y < self.release_y:
                self.dropping = True
                self.chess_y += self.chess_y_vel

        if not self.check_column_full(self.column):
            new_chess = Chess(self.column*self.UNIT +
                              self.HALF_UNIT, self.chess_y,
                              self.chess_color(), self.player_1)
            new_chess.draw_me()

            if self.chess_y >= self.release_y and \
                    self.chess_y > self.HALF_UNIT:
                self.chesses[self.column][self.check_release_spot(
                    self.column)] = new_chess
                # self.chess_board[self.column][self.row] = 1
                self.change_player()
                self.intact = False
                self.dropping = False

    def hold_and_drop_ai(self, col):
        '''
        To act the pressing and droping move for ai player
        '''
        self.intact = False
        self.column_ai = col
        chess_x = self.column_ai*self.UNIT+self.HALF_UNIT
        self.row_ai = self.check_release_spot(self.column_ai)
        self.release_y_ai = (self.row_ai+1)*self.UNIT + self.HALF_UNIT
        if self.chess_y_ai < self.release_y_ai:
            self.chess_y_ai += self.chess_y_vel

        if not self.check_column_full(self.column_ai):
            new_chess = Chess(chess_x, self.chess_y_ai,
                              self.chess_color(), self.player_1)
            new_chess.draw_me()

            if self.chess_y_ai >= self.release_y_ai and \
                    self.chess_y_ai > self.HALF_UNIT:
                self.chesses[self.column_ai][self.row_ai] = new_chess
                # self.chess_board[self.column_ai][self.row_ai] = 2
                self.change_player()
                self.chess_y_ai = self.HALF_UNIT
                self.ai_dropping = False
                self.col = -1

    def chess_color(self):
        '''
        To determine the color for a certain player
        '''
        COLOR_RED = color(255, 0, 0)
        COLOR_YELLOW = color(255, 255, 0)

        if self.player_1:
            chess_color = COLOR_RED
        else:
            chess_color = COLOR_YELLOW
        return chess_color

    def change_player(self):
        """ change player between
        player human and player ai """
        if self.player_1:
            self.player_1 = False
        else:
            self.player_1 = True

    def check_release_spot(self, column):
        """ check possible release spot
        in a certain column
        Integer -> Integer """
        for i in range(len(self.chesses[column])):
            if(self.chesses[column][i] is not None):
                return i-1
        return len(self.chesses[column])-1

    def check_game_end(self):
        """ check whether the board is full
        None -> Boolean """
        for column in self.chesses:
            for spot in column:
                if spot is None:
                    return False
        return True

    def check_column_full(self, column):
        """ check whether a certain column is full
        Integer -> Boolean """
        for spot in self.chesses[column]:
            if spot is None:
                return False
        return True

    def check_mouse_area(self):
        '''
        The mouse area will be restricted only right above the
        chess board.
        '''
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
        '''
        Display information when no place for a chess to put
        '''
        TEXT_COLOR = 0
        TEXT_SIZE = 80

        TEXT_X = 125
        TEXT_Y = 50

        fill(TEXT_COLOR)
        textSize(TEXT_SIZE)
        text("GAME OVER", TEXT_X, TEXT_Y)

    def check_winner(self):
        """ check the winner for the game
        None -> Boolean / None """
        columns = int(self.w/self.UNIT)
        rows = int(self.h/self.UNIT - 1)
        for i in range(columns):
            for j in range(rows-3):
                if self.chesses[i][j] is not None:
                    if (self.chesses[i][j+1] is not None and
                        self.chesses[i][j].player ==
                            self.chesses[i][j+1].player and
                            self.chesses[i][j+2] is not None and
                            self.chesses[i][j].player ==
                            self.chesses[i][j+2].player and
                            self.chesses[i][j+3] is not None and
                            self.chesses[i][j].player ==
                            self.chesses[i][j+3].player):
                        return self.chesses[i][j].player
        for i in range(columns-3):
            for j in range(rows):
                if self.chesses[i][j] is not None:
                    if (self.chesses[i+1][j] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+1][j].player and
                        self.chesses[i+2][j] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+2][j].player and
                        self.chesses[i+3][j] is not None and
                        self.chesses[i][j].player ==
                            self.chesses[i+3][j].player):
                        return self.chesses[i][j].player
        for i in range(columns-3):
            for j in range(rows-3):
                if self.chesses[i][j] is not None:
                    if (self.chesses[i+1][j+1] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+1][j+1].player and
                        self.chesses[i+2][j+2] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+2][j+2].player and
                        self.chesses[i+3][j+3] is not None and
                        self.chesses[i][j].player ==
                            self.chesses[i+3][j+3].player):
                        return self.chesses[i][j].player
        for i in range(columns-3):
            for j in range(3, rows):
                if self.chesses[i][j] is not None:
                    if (self.chesses[i+1][j-1] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+1][j-1].player and
                        self.chesses[i+2][j-2] is not None and
                        self.chesses[i][j].player ==
                        self.chesses[i+2][j-2].player and
                        self.chesses[i+3][j-3] is not None and
                        self.chesses[i][j].player ==
                            self.chesses[i+3][j-3].player):
                        return self.chesses[i][j].player
        return None

    def win_display(self, player):
        """ if a winner is selected, show certain information
        on the window."""
        TEXT_COLOR = 0
        TEXT_SIZE = 100

        TEXT_X = 125
        TEXT_Y = 350

        if player is True:
            fill(TEXT_COLOR)
            textSize(TEXT_SIZE)
            strokeWeight(3)
            text("RED WINS", TEXT_X, TEXT_Y)

        elif player is False:
            TEXT_X = 25
            fill(TEXT_COLOR)
            textSize(TEXT_SIZE)
            strokeWeight(3)
            text("YELLOW WINS", TEXT_X, TEXT_Y)

    # def winning_move(self, board, piece):
    #     # Check horizontal locations for win
    #     for c in range(self.column_total-3):
    #         for r in range(self.row_total):
    #             if (board[c][r] == piece and board[c+1][r] == \
    #                   piece and board[c+2][r] == \
    #               piece and board[c+3][r] == piece):
    #                 return True

    #     # Check vertical locations for win
    #     for c in range(self.column_total):
    #         for r in range(self.row_total-3):
    #             if (board[c][r] == piece and \
    #               board[c][r+1] == piece and \
    #               board[c][r+2] == piece and \
    #               board[c][r+3] == piece):
    #                 return True

    #     # Check positively sloped diaganols
    #     for c in range(self.column_total-3):
    #         for r in range(self.row_total-3):
    #             if (board[c][r] == piece and \
    #               board[c+1][r+1] == piece and \
    #               board[c+2][r+2] == piece and \
    #               board[c+3][r+3] == piece):
    #                 return True

    #     # Check negatively sloped diaganols
    #     for c in range(self.column_total-3):
    #         for r in range(3, self.row_total):
    #             if (board[c][r] == piece and \
    #               board[c+1][r-1] == piece and \
    #               board[c+2][r-2] == piece and \
    #               board[c+3][r-3] == piece):
    #                 return True

    # def evaluate_window(self, window, player):
    #     score = 0
    #     opp_player = self.player_human
    #     if player == self.player_human:
    #         opp_player = self.player_ai

    #     if window.count(player) == 4:
    #         score += 100
    #     elif window.count(player) == 3 and window.count(0) == 1:
    #         score += 5
    #     elif window.count(player) == 2 and window.count(0) == 2:
    #         score += 2

    #     if window.count(opp_player) == 3 and window.count(0) == 1:
    #         score -= 4

    #     return score

    # def score_position(self, board, player):
    #     score = 0

    #     center_array = [int(i) for i in list(board[self.column_total//2])]
    #     center_count = center_array.count(player)
    #     score += center_count * 3

    #     # Score Horizontal
    #     row_array = []
    #     for c in range(self.column_total-3):
    #         for r in range(self.row_total):
    #             window = [board[c+i][r] for i in range(4)]
    #             score += self.evaluate_window(window, player)

    #     # Score Vertical
    #     for c in range(self.column_total):
    #         for r in range(self.row_total-3):
    #             window = [board[c][r+i] for i in range(4)]
    #             score += self.evaluate_window(window, player)

    #     # Score positive sloped diagonal
    #     for r in range(self.row_total-3):
    #         for c in range(self.column_total-3):
    #             window = [board[c+i][r+i] for i in range(4)]
    #             score += self.evaluate_window(window, player)

    #     # Score positive sloped diagonal
    #     for c in range(self.column_total-3):
    #         for r in range(self.row_total-3):
    #             window = [board[c+i][r+3-i] for i in range(4)]
    #             score += self.evaluate_window(window, player)

    #     print(score)
    #     return score

    # def is_terminal_node(self, board):
    #     return self.winning_move(board, self.player_human) or
    #  self.winning_move(board, self.player_ai) or
    #  len(self.get_valid_locations(board)) == 0

    # def is_valid_location(self, board, col):
    #     return board[col][self.row_total-1] == 0

    # def get_valid_locations(self, board):
    #     valid_locations = []
    #     for col in range(self.column_total):
    #         if self.is_valid_location(board, col):
    #             valid_locations.append(col)
    #     return valid_locations

    # def get_next_open_row(self, board, col):
    #     for r in range(self.row_total):
    #         if board[col][r] == 0:
    #             return r

    # def minimax(self, board, depth, alpha, beta, maximizingPlayer):
    #     valid_locations = self.get_valid_locations(board)
    #     is_terminal = self.is_terminal_node(board)
    #     if depth == 0 or is_terminal:
    #         if is_terminal:
    #             if self.winning_move(board, self.player_ai):
    #                 return (None, 100000000000000)
    #             elif self.winning_move(board, self.player_human):
    #                 return (None, -10000000000000)
    #             else:  # Game is over, no more valid moves
    #                 return (None, 0)
    #         else:  # Depth is zero
    #             self.ai_dropping = True
    #             return (None, self.score_position(board, self.player_ai))

    #     if maximizingPlayer:
    #         value = -100000000000
    #         column = random.choice(valid_locations)
    #         for col in valid_locations:
    #             row = self.get_next_open_row(board, col)
    #             b_copy = copy.deepcopy(board)
    #             new_score = self.minimax(
    #                 b_copy, depth-1, alpha, beta, False)[1]
    #             if new_score > value:
    #                 value = new_score
    #                 column = col
    #             alpha = max(alpha, value)
    #             if alpha >= beta:
    #                 break
    #         print(column, value)
    #         return column, value

    #     else:  # Minimizing player
    #         value = 100000000000
    #         column = random.choice(valid_locations)
    #         for col in valid_locations:
    #             row = self.get_next_open_row(board, col)
    #             b_copy = copy.deepcopy(board)
    #             new_score = self.minimax(b_copy,
    #               depth-1, alpha, beta, True)[1]
    #             if new_score < value:
    #                 value = new_score
    #                 column = col
    #             beta = min(beta, value)
    #             if alpha >= beta:
    #                 break
    #         return column, value
