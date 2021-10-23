from ngram_frequencies import NgramFrequencies

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" Test every method in NgramFrequencies Class """

# Basic variables to input in Class NgramFrequencies
input_sentences_list = [
    ["hello", "i", "am", "tom"], ["i", "am", "happy", "to", "meet", "you"]]
input_number = 2

nf = NgramFrequencies(input_sentences_list, input_number)


def test_collect_words():
    """ Test collect words function """

    conc1 = {"hello_i": 1,
             "i_am": 2,
             "am_tom": 1,
             "am_happy": 1,
             "happy_to": 1,
             "to_meet": 1,
             "meet_you": 1
             }
    assert nf.collect_words(2) == conc1


def test_add_item():
    """ Test add item function """

    dict_test_1 = {
        "high": 1,
    }

    key_name_1 = "high"
    key_name_2 = "low"

    dict_output = nf.add_item(dict_test_1, key_name_1)
    assert dict_output == {"high": 2}

    dict_output = nf.add_item(dict_test_1, key_name_2)
    assert dict_output == {"high": 2, "low": 1}


def test_top_n_counts():
    """ Test top n counts function """

    conc2 = [("i_am", 2), ("hello_i", 1), ("am_tom", 1)]
    assert nf.top_n_counts(3) == conc2

    conc3 = [("i_am", 2), ("hello_i", 1), ("am_tom", 1), ("am_happy", 1)]
    assert nf.top_n_counts(4) == conc3


def test_top_n_freqs():
    """ Test top n freqs function """

    nf.total_count = 0
    conc4 = [("i_am", 0.25), ("hello_i", 0.125), ("am_tom", 0.125)]
    assert nf.top_n_freqs(3) == conc4

    nf.total_count = 0
    conc5 = [("i_am", 0.25), ("hello_i", 0.125),
             ("am_tom", 0.125), ("am_happy", 0.125)]
    assert nf.top_n_freqs(4) == conc5


def test_frequency():
    """ Test frenquency function """

    dict_test = {
        "high": 1,
        "medium": 2,
        "low": 3
    }

    total_count = 6
    nf.frequency(dict_test, total_count)

    assert dict_test == {
        "high": 0.167,
        "medium": 0.333,
        "low": 0.5
    }


def test_sort_by_reverse():
    """ Test sort by reverse function """

    dict_test = {
        "high": 1,
        "medium": 2,
        "low": 3
    }
    assert nf.sort_by_reverse(dict_test) == [(
        "low", 3), ("medium", 2), ("high", 1)]
