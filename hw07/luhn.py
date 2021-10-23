""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


""" This program is to check whether an input number is valid
using the Luhn's algorithm """

# Basic constants
FACTOR_OF_MUTIPLE_OF_TWO = 2
DOUBLE_THE_DIGIT = 2
CONSTANT_TO_CHECK_IF_LARGER_THAN_NINE = 9
DIFFERENCE_BETWEEN_SUM_OF_TWO_DIGITS_AND_ITSELF = 9


def receive_lagal_number():
    # This function is to make sure there is no special symbols or
    # alphaberic characters in the input.
    number = input(
        "Give a number to check if it is valid using Luhn's algorithm:\n")
    while True:
        try:
            int(number)
            break
        except ValueError:
            number = input("Please enter a correct number:\n")
    return number


def get_sum(number):
    # This function is to get the sum using Luhn's algorithm.
    # The main idea is that: the sum of the two digits of a number
    # is 9 larger than the number itself.
    sum = 0
    index = 0
    for character in reversed(number):  # get reverse of input
        if(index % FACTOR_OF_MUTIPLE_OF_TWO == 0):
            sum += int(character)
        else:
            number = DOUBLE_THE_DIGIT * int(character)
            if (number > CONSTANT_TO_CHECK_IF_LARGER_THAN_NINE):
                sum += number - DIFFERENCE_BETWEEN_SUM_OF_TWO_DIGITS_AND_ITSELF
            else:
                sum += number
        index += 1
    return sum


def check(number):
    # This function is check whether the output can be evenly
    # divided by 10.
    if get_sum(number) % 10 == 0:
        print(f"{number} is valid")
    else:
        print(f"{number} is invalid")


def main():
    # Process controller
    number_input = receive_lagal_number()
    check(number_input)


main()
