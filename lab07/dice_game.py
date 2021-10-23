from game_controller import GameController

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" Main function prints out rules and controls the main process
of dice game. """


def main():
    rules()
    gc = GameController()
    gc.dice_game()


def rules():
    print("--------------------------------\n" +
          "Welcome to street craps!\n\nRules:\n" +
          "If you roll 7 or 11 on your first roll, you win.\n" +
          "If you roll 2, 3, or 12 on your first role, you lose.\n" +
          "If you roll anything else, that's your 'point', and\n" +
          "you keep rolling until you either roll your point\n" +
          "again (win) or roll a 7 (lose)\n\n")


main()
