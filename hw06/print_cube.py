""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" This program aims to create a 3-dimension cube
with the help of list """


# The main function


def main():
    clean_drawing_board = create_drawing_board()
    draw_whole_pics(clean_drawing_board)


# Basic constants:
HALF_VALUE = 1/2
DOUBLE_VALUE = 2
TRIPLE_VALUE = 3

# Drawing symbols:
CORNER = "+"
INCLINED_LINE_ONE = "/"
VERTICAL_LINE_ONE = "|"
HORIZONTAL_LINE_ONE = "-"
SPACE = " "

# Needed values:
height = int(input("Input cube size (multiple of 2): "))
width = DOUBLE_VALUE*height
corner_height = 1
corner_width = 1
inclined_width = int(height*HALF_VALUE)  # width on the right side

# Total height of cube viewed in 2-dimension
total_height = TRIPLE_VALUE*corner_height + height + inclined_width

# Total width of cube viewed in 2-dimension
total_width = TRIPLE_VALUE*corner_height + inclined_width + inclined_width

# Function below create a list,
# with length of total_height


def create_drawing_board():

    list_input = []
    for _ in range(0, total_height+1):
        list_input.append("")
    return list_input


# This function accumulates all the parts below,
# and print out the whole cube


def draw_whole_pics(list_input):
    list_input = draw_horizontal_lines(list_input)
    list_input = draw_upper_width(list_input)
    list_input = draw_front_vertical_lines(list_input)
    list_input = draw_back_vertical_line(list_input)
    list_input = draw_bottom_width(list_input)
    for i in range(len(list_input)):
        print(list_input[i])

# Function below draws the two vertical lines
# On the front side


def draw_front_vertical_lines(list_input):
    for i in range(inclined_width+DOUBLE_VALUE*corner_height,
                   total_height-corner_height):
        for j in range(width+DOUBLE_VALUE*corner_width):
            if(j == 0 or j == width+corner_width):
                list_input[i] += VERTICAL_LINE_ONE
            else:
                list_input[i] += SPACE
    return list_input

# Function below draws the one vertical line
# On the right side


def draw_back_vertical_line(list_input):
    for i in range(corner_height, height+corner_height):
        k = i - 1
        if(k <= inclined_width):
            while(k > 0):
                list_input[i] += SPACE
                k -= 1
        else:
            for _ in range(inclined_width):
                list_input[i] += SPACE
        list_input[i] += VERTICAL_LINE_ONE
    return list_input

# Function below is used to create
# a horizontal line


def draw_horizontal_line(line):
    line += CORNER
    for _ in range(corner_width, width+corner_width):
        line += HORIZONTAL_LINE_ONE
    line += CORNER
    return line

# Function below draws the three vertical lines
# in the cube


def draw_horizontal_lines(list_input):
    for _ in range(inclined_width+corner_width):
        list_input[0] += SPACE
    list_input[0] = draw_horizontal_line(list_input[0])
    list_input[inclined_width +
               corner_width] = draw_horizontal_line(
                   list_input[inclined_width+corner_width])
    list_input[total_height -
               corner_height] = draw_horizontal_line(
                   list_input[total_height-corner_height])
    return list_input

# Function below draws the two inclined lines
# on the top


def draw_upper_width(list_input):
    for i in range(corner_width, inclined_width+corner_width):
        k = inclined_width - i + 1
        while(k > 0):
            list_input[i] += SPACE
            k -= 1
        list_input[i] += INCLINED_LINE_ONE
        for _ in range(width):
            list_input[i] += SPACE
        list_input[i] += INCLINED_LINE_ONE
    return list_input

# Function below draws the two inclined lines
# on the right side


def draw_bottom_width(list_input):
    for i in range(height+corner_height, total_height-corner_height):
        k = total_height - i - DOUBLE_VALUE*corner_height
        while(k > 0):
            list_input[i] += SPACE
            k -= 1
        if(i == height+corner_height):
            list_input[i] += CORNER
        else:
            list_input[i] += INCLINED_LINE_ONE
    return list_input


main()
