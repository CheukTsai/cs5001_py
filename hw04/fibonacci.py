# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# for this exercise, N == 1 and N == 2 are also included.

import sys
def main():
    length = int(sys.argv[1]) 
    if(length<=0): # make sure the program will not receive non-positive numbers
        print("Input number should be positive. Please restart the program")
        sys.exit()
    list_output = []
    temp = 1
    while(temp<=length):
        if(temp == 1): # when N == 1, the fibonacci number will be 0
            list_output.append(0)
        elif(temp == 2): # when N == 2, the fibonacci numbers will be 0 and 1 
            list_output.append(1)
        else:
            num_new = list_output[-1] + list_output[-2] # sum up the last two numbers
            list_output.append(num_new)
        temp += 1
    print(list_output)
main()