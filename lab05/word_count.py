# Credited by Zhuocai Li
# https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi

import re


def main():

    # Get the pattern (all words without space).
    pattern_no_space = re.compile(r"\S+")
    # Get the pattern (all words (with only a-zA-Z0-9) without space).
    pattern_letters_and_numbers = re.compile(r"\w")
    while True:  # Make sure the file is input correctly.
        try:
            input_file = input("Please enter the file name: ")
            raw_file = open(input_file)
            break
        except FileNotFoundError:
            print("Can't open", input_file)

    # Get ready to collect output data.
    count_words = 0
    count_letters_and_numbers = 0
    count_characters = 0

    for line in raw_file:
        line = line.rstrip()

        # Use the patterns above to find the collect the words into lists.
        edited_line_list_no_space = pattern_no_space.findall(line)
        edited_line_list_letters_and_numbers
        = pattern_letters_and_numbers.findall(
            line)
        for word in edited_line_list_no_space:
            count_characters += len(word)
        count_words += len(edited_line_list_no_space)
        count_letters_and_numbers += len(edited_line_list_letters_and_numbers)

    # Print out information.
    print("Words:", count_words)
    print("Characters:", count_characters)
    print("Letters & numbers:", count_letters_and_numbers)


main()
