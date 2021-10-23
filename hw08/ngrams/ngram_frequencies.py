import sys
from text_cleaner import TextCleaner

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


class NgramFrequencies:

    def __init__(self, sentences, number):
        """ The constructor of NgramFrequencies"""
        self.total_count = 0
        self.n = number
        self.sentences = sentences

    def collect_words(self, number):
        """
        To generate grams in needed format
        Integer -> Dictionary
        """

        data = {}
        length = number - 1

        for sentence in self.sentences:
            for i in range(len(sentence)-length):
                remaining_number_of_word = length
                gram = sentence[i]
                step = i

                while(remaining_number_of_word > 0):
                    # Set the output in certain format
                    step += 1
                    gram += "_"
                    gram += sentence[step]
                    remaining_number_of_word -= 1

                data = self.add_item(data, gram)
                self.total_count += 1

        return data

    def add_item(self, dict_input, key_name):
        """
        To add key or change value in dictionary
        (Takes an n-gram and increments its count in the dictionary)

        Dictionary, String -> Dictionary
        """

        if key_name in dict_input.keys():
            dict_input[key_name] += 1
        else:
            dict_input[key_name] = 1
        return dict_input

    def top_n_counts(self, number):
        """
        Returns a list of items sorted on the count,
        with the most frequent first

        Integer -> List
        """

        self.collect_words(self.n)
        data = self.collect_words(self.n)
        output = self.sort_by_reverse(data)
        return output[0:number]

    def top_n_freqs(self, number):
        """
        Returns a similar list as above,
        but with frequencies instead of counts.

        Integer -> List
        """

        data = self.collect_words(self.n)
        self.frequency(data, self.total_count)
        output = self.sort_by_reverse(data)
        return output[0:number]

    def frequency(self, dict_input, total_count):
        """
        Changes the value in dictionary from counts to freqs
        """
        for k in dict_input.keys():
            dict_input[k] = round(dict_input[k]/total_count, 3)

    def sort_by_reverse(self, dict_input):
        """
        A function to sort dict by decreasing order of its values

        Dictonary -> List
        """

        return sorted(
            dict_input.items(),
            key=lambda x: x[1],
            reverse=True)
