# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# for this program, we are trying to offer you a special ID system,
# after your 1. first name; 2. last name; and 3. favorite word are input
# you will receive a user name and 3 recommended passwords!


import random

# concatenation() is to use similar-looking symbols to replace characters in the input string


def concatenation(word_input):
    # transform the input string to lower case to simplify the following work
    word_input = word_input.lower()
    word_input = word_input.replace("a", "@")
    word_input = word_input.replace("o", "0")
    word_input = word_input.replace("l", "1")
    word_input = word_input.replace("s", "$")
    return word_input

# acronym() is to get 1. the lower case of the first character and
# 2. the upper case of last character of the input string


def acronym(word_input):
    word_output = word_input[0].lower()+word_input[-1].upper()
    return word_output

# random_length() is to get a random-length substring of the input string
# with the least length of 1


def random_length(word_input):
    final_length = random.randint(1, len(word_input))
    word_output = word_input[0:final_length]
    return word_output

# the main function of this program


def main():

    # receive input information
    print("Welcome to the username and password generator!")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    fav_word = input("Please enter your favorite word: ")

    # create user name
    user_name = first_name.lower()[0] + last_name.lower()
    count_last_name = len(last_name)
    while(count_last_name < 7):  # if last name is shorter than 7, fill with "*"
        user_name += "*"
        count_last_name += 1
    # add a random integer (0-99) at the end of the user name
    user_name += str(random.randint(0, 99))

    # rule for password 1
    password1 = concatenation(
        last_name)+str(random.randint(0, 99))+concatenation(first_name)

    # rule for password 2
    password2 = acronym(last_name)+acronym(first_name)+acronym(fav_word)

    # rule for password 3
    password3 = random_length(
        last_name) + random_length(fav_word) + random_length(first_name)

    # print out results with some empty lines
    print("")
    print("Thanks", first_name, ", your user name is", user_name)
    print("")
    print("Here are three suggested passwords for you to consider:")
    print("")
    print("Password 1:", password1)
    print("Password 2:", password2)
    print("Password 3:", password3)


main()
