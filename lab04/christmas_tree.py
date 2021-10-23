# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

number_input = int(input("Please enter an odd number to create a christmas tree: "))

# check if an odd number is received
while(number_input % 2 == 0):
    print("Please enter an odd number.")
    number_input = int(input("Please enter an odd number to create a christmas tree: "))

def main():
    line = ""
    half = int((number_input+1)/2) # getting the middle x
    for num_h in range(1,half+1):
        for num_w in range(1,number_input+1):
            
            # the first row is sepecial, with only a "*"
            if (num_h == 1 and num_w == (number_input+1)/2):
                line += "*"
            
            # the last row is sepecial, with "_______" as tree's bottom
            elif(num_h == (number_input+1)/2):
                if(num_w == 1):
                    line += "/"
                elif(num_w == number_input):
                    line += "\\"
                else:
                    line += "_"
            
            # for other rows
            else:
                if(num_w == half-num_h+1):
                    line += "/"
                elif(num_w == half+num_h-1):
                    line += "\\"
                else:
                    line += " "
        print(line)
        line = ""

main()

