""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi"""


""" This program is developed to create a rocket by certain requirement,
class BuildRocket is used, so that every part of the rocket can be printed out independently,
and the main() function would be much clearer."""


# Basic needed constants:
import sys
INCREMENT_BY_TWO = 2
HALF_DIVIDEND = 2
SYS_ARGV_LENGTH_2_CHECKER = 2
SYS_ARGV_LENGTH_3_CHECKER = 3

# All rocket-building related functions(methods) are built in class BuildRocket


class BuildRocket:

    # Initialize the data-type
    list_to_draw = []
    width = 0
    times = 0
    striped = ""

    # The "complier":
    # Receiving 3 inputs: n1(int), n2(int) and info(string)
    # Then initialize values that can be only used inside the class
    # including: width, times and the information determining whether the rocket neeeded to be striped.
    def __init__(self, n1, n2, info):
        self.width = n1
        self.times = n2
        self.striped = info

    # Using __ to make draw function private
    # draw function is to print out lists that collect all the lines to-be-draw
    def __draw(self, list_to_draw):
        for line in list_to_draw:
            print(line)

    # Is_striped function is to check whether the rocket is required to be striped,
    # Return boolean
    def __is_striped(self):
        if(self.striped == "striped"):
            return True

    # The rectangle body part is constructed by two parts:
    # one is to create a single part
    # the other is to multiple several times
    # Though this two parts can be written in a nested for loop
    # But this time, I want to make the functions much clearer,
    # so that I divided them into two parts.
    def __create_body_part_list(self):
        list_part = []
        num_input = self.width
        num_potential_half = 0

        if(self.__is_striped()):
            # If the rocket is striped, then the upper part of the rocket is changed
            num_potential_half = int(num_input/2)
            for _ in range(num_potential_half):
                line = ""
                for _ in range(num_input):
                    line += "_"
                list_part.append(line)

        # If the rocket is striped, the range of the "x" lines would be (int(width/2),width);
        # If not, range would be (0,width)
        for _ in range(num_potential_half, num_input):
            line = ""
            for _ in range(num_input):
                line += "x"
            list_part.append(line)

        return list_part  # return a list

    # This is a public method to draw the whole body
    # Mutiple several times of a part and print it out
    def draw_whole_body(self):
        list_multi = []
        num_input = self.times
        list_part = self.__create_body_part_list()

        # Create the whole body.
        # Can be a little bit over-complicated
        # Since I need to itearte the list once again.
        # But maybe clearer.
        for _ in range(num_input):
            for j in range(len(list_part)):
                list_multi.append(list_part[j])

        # Instead of retuning a value,
        # Directly print it out.
        self.__draw(list_multi)

    # A public function to seperately draw the head (nose)
    def draw_head(self):
        list_multi = []
        num_input = self.width
        num_final = int(num_input/HALF_DIVIDEND)

        for i in range(num_final):
            line = ""
            empty_distance = num_final-i  # Get the index of the first star
            for j in range(num_input):
                if(j > empty_distance-1 and j <= num_input-empty_distance-1):
                    line += "*"
                else:
                    line += " "
            list_multi.append(line)

        self.__draw(list_multi)

    # A public function to seperately draw the tail
    # The start index would require the floor quarter of the input width
    def draw_tail(self):
        list_multi = []
        num_input = self.width
        half = num_input // HALF_DIVIDEND
        line = ""
        first_line = half

        # value half increments until the program prints out a line that is as long as width
        while(half < num_input+INCREMENT_BY_TWO):
            line = ""
            empty_distance = first_line - half // HALF_DIVIDEND
            for j in range(num_input):
                if(j >= empty_distance and j < num_input-empty_distance):
                    line += "*"
                else:
                    line += " "

            # The length of the stars increments by 2 everytime.
            half += INCREMENT_BY_TWO
            list_multi.append(line)

        # The tail required another line that is as long as the width.
        list_multi.append(line)

        self.__draw(list_multi)

    def draw_rocket(self):
        self.draw_head()
        self.draw_whole_body()
        self.draw_tail()

# check_sys_argv() function is to check 1. enough info is input;
# 2. if there is a "striped" info input
# return a list containing three info (width, times, striped)


def check_sys_argv():
    output_list = []
    striped = ""

    if(len(sys.argv) <= SYS_ARGV_LENGTH_2_CHECKER):
        print("Please give enough information!!!")
        sys.exit()  # Without enough info (only with 1 value input), quit the program
    else:
        width = int(sys.argv[1])
        times = int(sys.argv[2])

    if(len(sys.argv) > SYS_ARGV_LENGTH_3_CHECKER):
        striped = sys.argv[-1]

    output_list.append(width)
    output_list.append(times)
    output_list.append(striped)

    return output_list

# Main function of this program


def main():
    input_info = check_sys_argv()
    go_rocket = BuildRocket(input_info[0], input_info[1], input_info[2])
    go_rocket.draw_head()


main()
