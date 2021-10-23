# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# Background: I try to create one to check squares of arbitrary sizes, but
# there is a little problem: like for a 4*4 square,
# it is hard to tell whether the number input "111167" will be 1 11 16 7 or 11 1 16 7
# if this can be solved, I can try to present one.

# At the bottom is the code for 3*3 square, using fixed length 3 and fixed value 15 


SUM_CORRECT = 15 # fixed number for value checking for 3*3 square
ALL_LENGTH = 3 # fixed number for row/column/corner to corner length

# magic_number() is used for enetering numbers for each row, return list containg int(numbers) in each row
def magic_number(): 
    number = input("")
    list_row = []
    for char in number:
        list_row.append(int(char))
    return list_row

list_unchecked = []

# OPTIONAL: NUMBER CHECKING
# check() is used to check if numbers input are probelmatic,while problems can be:
# 1. not enough or over 9 numbers
# 2. not all numbers from 1-9 included

# The solution is to create a check-list with the length of all integers(1-9) input,
# check_list will be first filled with 0
# if an integer is input, the corresponding position (num-1) will add 1
# if and only if 1-9 are all input, the check-list will be filled with 1, and check() will return True
# else check() will return False

def check(list_input):
    check_list = []
    for _ in range(0,ALL_LENGTH*ALL_LENGTH):
        check_list.append(0)
    for num in list_input:
        if(num == 0):
            return False
        check_list[num-1] += 1
        if(check_list[num-1]!=1):
            return False
    return True

# enter_number() is used for collect all 3 3-digits numbers
def enter_number():   
    # Collecting numbers
    list_numbers = [] # list_numbers is used to collect all numbers in form of [[x,x,x],[x,x,x],[x,x,x]]
    list_unchecked = [] # list_unchecked is used for later checking if all numbers from 1 to 9 are included, in form of [x,x,x,x,x,x,x,x,x]
    number_enter_times = 1
    check_flag = False
    while(check_flag == False):

        while (number_enter_times <= ALL_LENGTH):
            list_numbers.append(magic_number())
            number_enter_times += 1
        
        for row in list_numbers:
            for number in row:
                list_unchecked.append(number)
       
        if(check(list_unchecked) == True):
            check_flag = True
        
        else:
            print("Your numbers should include all 9 numbers from 1 to 9")
            print("Please re-enter your numbers")
            list_numbers = []
            list_unchecked = []
            number_enter_times = 1
    return list_numbers

# row test function is to check if all 3 rows equal 15, return boolean
def row_test(list_input): 
    sum_temp = 0
    for rows in list_input:
        for i in range(0,len(rows)):
            sum_temp += rows[i]
        if (sum_temp != SUM_CORRECT):  
            return False
        sum_temp = 0
    return True

# column test function is to check if all 3 columns equal 15, return boolean
def column_test(list_input):
    sum_temp = 0
    for i in range(0, len(list_input)):
        for rows in list_input:
            sum_temp += rows[i]
        if (sum_temp != SUM_CORRECT): 
            return False
        sum_temp = 0
    return True

# c2c(corner to corner) test function is to check if both 2 corner-to-corner equal 15, return boolean
def c2c_test(list_input):
    sum_temp = 0
    end_num = len(list_input)-1

    #right-top to left-bottom
    for i in range(0, len(list_input)):
        sum_temp += list_input[i][end_num]
        end_num -= 1
    if(sum_temp != SUM_CORRECT): 
        return False
    
    #left-top to right-bottom
    end_num = 0
    sum_temp = 0
    for i in range(0, len(list_input)):
        sum_temp += list_input[i][end_num]
        end_num += 1
    if(sum_temp != SUM_CORRECT):    
        return False
    return True

# main function for magic square validator
def main():
    print("Enter a magic number") 
    list_test = enter_number()
    if(column_test(list_test) and row_test(list_test) and c2c_test(list_test)):
        print("This is a magic square!")
    else: 
        print("Not a magic square!")


main()