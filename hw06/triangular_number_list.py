""" Credited by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" This program aims at print out a list that carries
triagular numbers generated from the input numbers."""


def main():
    list_output = []  # Initialize a list to print

    while(True):
        word_input = input("Enter a number, or enter 'done': ")

        if(word_input.lower() == "done"):
            print(list_output)
            break

        # Length means how "far" should numbers be sumed up
        length = int(word_input)

        triangular_output = get_triangular_number(word_input, length)
        list_output.append(triangular_output)

        print("The triangular number for", length, "is", triangular_output)


def get_triangular_number(word_input, length):

    triangular_output = 0  # Initialzie an integer to carry the output
    for num in range(1, length+1):
        triangular_output += num
    return triangular_output


main()
