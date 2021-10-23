from game_controller import GameController
from chess import Chess

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


def test_constructor():
    """ test constructor of
    game controller """
    gc = GameController(700, 700)
    assert gc.score_file == {} and \
        gc.chess_y == 50 and \
        gc.chess_y_vel == 25 and \
        gc.chess_y_ai == 50 and \
        gc.column_ai == 0 and \
        gc.release_y == 0 and \
        gc.release_y_ai == 0 and \
        gc.row_ai == 0 and \
        gc.column is None and \
        gc.row == 0 and \
        gc.intact is False and \
        gc.mouse_press is False and \
        gc.player_1 is True and \
        gc.release is True and \
        gc.dropping is False and \
        gc.depth == 5 and \
        gc.name is None and \
        gc.winner_picked is False and \
        gc.chesses == [] and \
        gc.chess_board == [] and \
        gc.new_chess is None and \
        gc.col == -1 and \
        gc.ai_dropping is False


def test_top_n_counts():
    """ Test top counts function """
    gc = GameController(700, 700)
    gc.score_file = {"a": 1, "b": 2, "c": 3}
    assert gc.top_n_counts() == [('c', 3), ('b', 2), ('a', 1)]

    gc.score_file = {"a": 1, "c": 3, "b": 2}
    assert gc.top_n_counts() == [('c', 3), ('b', 2), ('a', 1)]


def test_initialize():
    """ test function initialize """
    gc = GameController(200, 300)
    gc.initialize()
    assert gc.chesses == [[None, None], [None, None]]

    gc = GameController(100, 100)
    gc.initialize()
    assert gc.chesses == [[]]

    gc = GameController(400, 500)
    gc.initialize()
    assert gc.chesses == [[None, None, None, None], [None, None, None, None],
                          [None, None, None, None], [None, None, None, None]]


def test_change_player():
    """ test function change player """
    gc = GameController(200, 300)
    gc.player_1 = True
    gc.change_player()
    assert gc.player_1 is False

    gc = GameController(200, 300)
    gc.player_1 = False
    gc.change_player()
    assert gc.player_1 is True


def test_check_release_spot():
    """ test function check release spot """
    gc = GameController(200, 300)
    gc.chesses = [[None, True, True], [None, None, False]]
    assert gc.check_release_spot(1) == 1
    assert gc.check_release_spot(0) == 0


def test_check_game_end():
    """ test function check game end """
    gc = GameController(200, 300)
    gc.chesses = [[None, True, True], [None, None, False]]
    assert gc.check_game_end() is False

    gc = GameController(200, 300)
    gc.chesses = [[True, True, True], [False, False, False]]
    assert gc.check_game_end() is True


def test_check_column_full():
    """ test function check column full """
    gc = GameController(200, 300)
    gc.chesses = [[True, True, True], [None, None, False]]
    assert gc.check_column_full(1) is False
    assert gc.check_column_full(0) is True


def test_check_winner():
    """ test function check winner """
    gc = GameController(700, 700)
    chess_t = Chess(0, 0, "color", True)
    chess_f = Chess(0, 0, "color", False)

    gc.chesses = [[None, None, chess_t, None, None, None],
                  [None, None, chess_t, None, None, None],
                  [None, None, chess_t, None, None, None],
                  [None, None, chess_t, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None]]
    assert gc.check_winner() is True

    gc.chesses = [[None, None, chess_f, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None]]
    assert gc.check_winner() is False

    gc.chesses = [[None, None, chess_t, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, chess_f, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None],
                  [None, None, None, None, None, None]]
    assert gc.check_winner() is None
