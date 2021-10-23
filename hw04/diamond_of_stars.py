# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# for this exercise, the difficult part is to ensure that 
# input numbers 2k and 2k-1 (k is an integer >= 1) will have the same width

import sys
def main():
    height = int(sys.argv[1])
    
    # The following two lines are to ensure that input numbers 2k and 2k-1 (k is an integer >= 1)
    # will get the same width of the diamond
    
    half = int((height+1)/2) 
    width = half*2-1
    
    line = ""
    for i in range(1,height+1):
        empty_distance = abs(int((height+1)/2-i)) # how far the first symbol will appear (empty_distance+1) for each line
        start_point = empty_distance
        end_point = width-empty_distance+1 # how far the last symbol will end (end_point-1) for each line
        for j in range(1,width+1):
            if(j > start_point and j < end_point):
                line += "*"
            else:
                line += " "
        print(line)
        line = ""
main()