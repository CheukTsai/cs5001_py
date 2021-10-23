from pair_of_dice import PairOfDice

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" GameController class controls the gaming process,
including roll dice and check the score."""


class GameController:
    WIN_LIST_1 = [7, 11]  # Win numbers for the first roll
    LOSE_LIST_1 = [2, 3, 12]  # Lose numbers for the first roll
    LOST_LIST_2 = [7]  # Lose numbers afterwards

    def __init__(self):
        self.win_list_1 = GameController.WIN_LIST_1
        self.lose_list_1 = GameController.LOSE_LIST_1
        self.lose_list_2 = GameController.LOST_LIST_2
        self.pod = PairOfDice()  # Calls Pair_of_Dice Class
        self.times = 0  # Check the times of rolling and scoring
        self.stop_sign = False  # Determine whether to stop or not

    # Rolling methods
    def rolling(self):
        input("Press enter to roll the dice...")
        print("")
        self.pod.current_value()
        self.attempt = self.pod.sum
        self.times += 1

    def scoring(self):
        if(self.times == 1):  # First time
            if(self.attempt in self.win_list_1):
                self.win()
            elif(self.attempt in self.lose_list_1):
                self.lose()
            else:  # Other times
                self.point = self.attempt
                print("Your point is", self.point)
        else:
            if(self.attempt == self.point):
                self.win()
            elif(self.attempt in self.lose_list_2):
                self.lose()
            else:
                print("You rolled", self.attempt)

    def win(self):
        print(f"You rolled {self.attempt}. You win!")
        self.stop_sign = True

    def lose(self):
        print(f"You rolled {self.attempt}. You lose.")
        self.stop_sign = True

    def dice_game(self):  # If win/lose, stop going on
        while(self.stop_sign is False):
            self.rolling()
            self.scoring()
