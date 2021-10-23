import re


""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" This module contains DataAnalysis class,
helping to analyse specific csv data. """


class DataAnalysis:
    """This calss is to analyse data from input file."""

    def __init__(self, file):
        self.file = file
        self.data = {
            "language": [],
            "email": []
        }
        self.read_data(self.file)
        self.DOMAIN_LENGTH = 2  # A restrict to find country domain.
        # TODO: set up the necessary instance variables
        pass

    def read_data(self, file_name):
        file = open(file_name)
        row_header = True
        for line in file:
            line = line.rstrip().split(",")
            if(row_header is True):
                self.lang_column = self.find_column(line, "language")
                self.email_column = self.find_column(line, "email")
                row_header = False
            else:
                self.data["language"].append(line[self.lang_column])
                email = line[self.email_column]
                self.data["email"].append(
                    re.findall(r'[^\.]\w+', email))
        # TODO: read the data and get the counts
        pass

    def top_n_lang_freqs(self, number):
        self.lang_freq = {}
        self.total_count_lang = len(self.data["language"])
        for item in self.data["language"]:
            self.add_key(self.lang_freq, item)
        self.divide_by_total(
            self.lang_freq, self.total_count_lang)
        lang_by_order = self.sort_by_reverse(
            self.lang_freq)
        return lang_by_order[0:number]
        # TODO:
        # Implement top_n_lang_freqs()
        # Should take a number N as an argument and return
        # an N-length list of tuples representing languages
        # and their frequencies in the data, ordered from
        # highest frequency to lowest.
        pass

    def top_n_country_tlds_freqs(self, number):
        self.country_tlds_freq = {}
        self.total_count_country = len(self.data["email"])
        for item in self.data["email"]:
            tlds = item[-1]
            if len(tlds) == self.DOMAIN_LENGTH:
                self.add_key(
                    self.country_tlds_freq, tlds)
        self.divide_by_total(
            self.country_tlds_freq, self.total_count_country)
        country_tlds_by_order = self.sort_by_reverse(
            self.country_tlds_freq)
        return country_tlds_by_order[0:number]

        # TODO:
        # Implement top_n_country_tlds_freqs()
        # Should take a number N as an argument and return
        # an N-length list of tuples representing country (2-letter)
        # top-level domain identifiers (e.g. 'jp', 'uk', 'cn', 'ca')
        # and their frequencies as email domains the data, ordered
        # from highest frequency to lowest.
        pass

    # TODO:
    # Implement any other necessary/helpful methods to support
    # the ones above.

    def add_key(self, dict_input, key_name):
        # A function to set key in dict.
        if key_name not in dict_input.keys():
            dict_input[key_name] = 1
        else:
            dict_input[key_name] += 1

    def sort_by_reverse(self, dict_input):
        # A function to sort dict by decreasing order of its values.
        return sorted(
            dict_input.items(),
            key=lambda x: x[1],
            reverse=True)

    def divide_by_total(self, dict_input, total_count):
        # A function to divide values by total count
        for k in dict_input.keys():
            dict_input[k] /= total_count

    def find_column(self, list_input, column_name):
        # A function to find the exact column with certain column name
        for i in range(len(list_input)):
            if list_input[i] == column_name:
                return i
