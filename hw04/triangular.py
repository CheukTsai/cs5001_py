# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# for this exercise, I add some space between the symbols in order to ensure the 
# structure of the triangular

import sys
def main():
    height = int(sys.argv[1]) # read the input number
    final_length = 2*height - 1 # the height of the last row
    line = "" 
    if(height < 1): # check if the number is legal
        print("Length should be no less than 1")
    else:
        for i in range(1,height+1): 
            for j in range(1,final_length+1):
                if((j >= height-i+1) and (j <= height+i-1)): 
                    if((j - (height - i + 1)) %2 == 0):
                        line += "o"
                    else:
                        line += " "
                else:
                    line += " "
            print(line)
            line = ""
main()
