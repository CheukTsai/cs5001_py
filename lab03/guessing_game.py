# Homework credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

import random
def GUESS():
    final_num = random.randint(1,50)
    print("I picked a number between 1 and 50. Try and guess!")
    guess_num = int(input(""))
    guess_times = 1
    print("You guessed ", guess_num)
    while (guess_num != final_num):
        
        # define the result and make it easier to print it out in the same pattern
        how = ""
        dif = abs(guess_num - final_num)
        if(dif <= 1):
            how = "scalding hot"
        elif(dif <= 2):
            how = "extremely warm"
        elif(dif <= 3):
            how = "very warm"
        elif(dif <= 5):
            how = "warm"
        elif(dif <=8):
            how = "cold"
        elif(dif <= 13):
            how = "very cold"
        elif(dif <= 20):
            how = "extremely cold"
        else:
            how = "icy freezing miserably cold"
        
        # every try will increase the number of guess
        guess_times = guess_times + 1
        print("Your guess is ", how)
        guess_num = int(input(""))
    print("Congratulations. You figured it out in ", guess_times, " tries.")
    
    # upgrading the game with mock or compliment
    if(guess_times == 1):
        print("That was lucky!")
    elif(guess_times <= 4):
        print("That was amazing!")
    elif(guess_times <= 6):
        print("That was okay.")
    elif(guess_times == 7):
        print("Meh.")
    elif(guess_times <= 9):
        print("This is not your game.")
    else:
        print("You are the worst guesser I've ever seen.")
GUESS()