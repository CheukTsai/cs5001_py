import sys
from data_analysis import DataAnalysis


""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" This module is to print out the data report. """

# Basic constants
RANK_TO_BE_INCLUDED = 10
DECIMAL_DIGITS = 3


def main(file_name):
    data = DataAnalysis(file_name)

    # Report top ten languages by frequency
    print("Languages:")
    print_output(data.top_n_lang_freqs(RANK_TO_BE_INCLUDED))

    # Report top ten country (2 letter) top
    # level domains by frequency
    print("Top level country domains:")
    print_output(data.top_n_country_tlds_freqs(RANK_TO_BE_INCLUDED))


def print_output(collection):
    for item in collection:
        print(item[0]+":  \t", round(item[1], DECIMAL_DIGITS))


main(sys.argv[1])
