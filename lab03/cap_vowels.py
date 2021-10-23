# Homework credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

def CV():
    word = str(input("Please enter your word: ")).lower()
    word_print = ""
    for letter in word:
        if(letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
            letter = letter.upper()
        word_print += letter
    print(word_print)
CV()