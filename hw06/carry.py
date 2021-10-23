""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" This program is used to get the sum of two integers and
how many carries happen during the operation """

# Basic constant:
VALUE_NEEDED_TO_CARRY = 10


def main():
    integer_1 = int(input("Enter the first number: "))
    integer_2 = int(input("Enter the second number: "))
    get_sum(integer_1, integer_2)
    get_carry_times(integer_1, integer_2)


def get_sum(input_1, input_2):
    print(input_1, "+", input_2, "=", input_1+input_2)


def get_carry_times(input_1, input_2):
    carry_time = 0
    # Should be calculated until the longer one
    # has been wholely iterated
    counted_range = max(len(str(input_1)), len(str(input_2)))
    # temp = 0 if carry is no need
    # Otherwise, temp = 1
    temp = 0

    for _ in range(counted_range):

        # Check the last digit
        if(input_1 % VALUE_NEEDED_TO_CARRY +
           input_2 % VALUE_NEEDED_TO_CARRY +
           temp >= VALUE_NEEDED_TO_CARRY):
            temp = 1
            carry_time += 1
        else:
            temp = 0

        # Go to next last digit
        input_1 //= VALUE_NEEDED_TO_CARRY
        input_2 //= VALUE_NEEDED_TO_CARRY

    print("Number of carries:", carry_time)


main()
