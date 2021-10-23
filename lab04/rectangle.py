# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

def main():
    symbol = input("Please enter your symbol: ")
    width = int(input("Please enter the width of your rectangle: "))
    height = int(input("Please enter the height of your rectangle: "))
    
    # Check if the width and height are proper
    if(width < 2 or height < 2):
        print("----------------------------------")
        print("Sorry, either your width or height should be no less than 2.")
        print("Please re-eneter all the information")
        print("----------------------------------")
        main()
    else:
        line = ""
        for num_h in range(1, height + 1):
            for num_w in range(1, width + 1):

                # except the first line and last line, all are the same
                if(num_h != 1 and num_h != height):
                    if(num_w != 1 and num_w != width):
                        line += " "
                    else:
                        line += symbol
                
                # the first line and last line are filled with symbols
                else:
                    line += symbol
            print(line)
            line = ""
main()