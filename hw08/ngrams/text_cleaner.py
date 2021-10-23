import re

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class TextCleaner:
    """ A processor to clean the input text """

    def __init__(self):
        # A constant to avoid collecting empty lines
        self.TO_AVOID_EMPTY_LIST = 1

    def cleasing(self, line):
        """
        Divides every line into seperate sentences,
        and collect every words in each sentence
        with certain rules.

        String -> List
        """

        data = []
        line = line.rstrip().lower()
        line = self.replace_abbreviate(line)
        line = self.replace_punctuation(line)
        sentences = line.split(".")

        for sentence in sentences:
            words_in_sentence = sentence.split()
            if(len(words_in_sentence) > self.TO_AVOID_EMPTY_LIST):
                data.append(words_in_sentence)
        return data

    def replace_abbreviate(self, line):
        """
        Get rid of the dot
        after some abbreviate

        String -> String
        """

        line = line.replace("mr.", "mr")
        line = line.replace("dr.", "dr")
        return line

    def replace_punctuation(self, line):
        """
        Change ',' to 'COMMA',
        and get rid of some punctuations

        String -> String
        """

        line = re.sub(",", " COMMA", line)
        line = re.sub(r"[^ .,'\w]", "", line)
        return line
