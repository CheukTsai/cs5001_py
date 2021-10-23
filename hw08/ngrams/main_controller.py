from ngram_frequencies import NgramFrequencies
from text_cleaner import TextCleaner
import sys

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" The main controller of the ngram frquencies generator program """

# Basic constants
RANK_NEEDED = 10
UNI = 1
BI = 2
TRI = 3

# An empty list ready to collect data
data = []


def main():
    # Giva warning if the input file name is wrong
    try:
        file_name = sys.argv[1]
        file_input = open(file_name)
    except FileNotFoundError:
        print("Can't find", file_name)
        return

    tc = TextCleaner()

    for line in file_input:
        sentences = tc.cleasing(line)
        for broke_sentence in sentences:
            data.append(broke_sentence)

    # Call classes individually
    unigrams = NgramFrequencies(data, UNI)
    bigrams = NgramFrequencies(data, BI)
    trigrams = NgramFrequencies(data, TRI)

    unigrams_output = unigrams.top_n_freqs(RANK_NEEDED)
    bigrams_output = bigrams.top_n_freqs(RANK_NEEDED)
    trigrams_output = trigrams.top_n_freqs(RANK_NEEDED)

    # Print out main output information
    print("Top", RANK_NEEDED, "unigrams:")
    print_by_line(unigrams_output)
    print("Top", RANK_NEEDED, "bigrams:")
    print_by_line(bigrams_output)
    print("Top", RANK_NEEDED, "trigrams:")
    print_by_line(trigrams_output)


def print_by_line(list_input):
    # Print out ranked information in clear format
    for item in list_input:
        print("\t", item)


main()
