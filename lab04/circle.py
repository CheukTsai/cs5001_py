# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

# How I treat this problem is to assume that this circle exists in an axis,
# with a radius of r, and the center is (r,-r), 
# since we are drawing the circle from top-left (0,0) to bottom-right (2r,-2r)
# then, the formula to create this circle will be (x-r)*(x-r)+(y-(-r))(y-(-r)) = r*r
# which is (x-r)*(x-r)+(y+r)(y+r) = r*r

import math
radius = int(input("Please enter your radius: "))
diam = 2*radius
def main():
    line = ""
    for x in range(1, diam+1):
        for y in range(1, -(diam+1), -1):
            if(math.sqrt((x-radius)*(x-radius)+(y+radius)*(y+radius))<radius):
                line += "o"
            else:
                line += " "
        print(line)
        line = ""
main()
