from text_cleaner import TextCleaner

""" Created by Zhuocai (Tsai) Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

""" Test every method in TextCleaner Class """

tc = TextCleaner()


def test_replace_abbreviate():
    """ Test replace abbreviate function """

    s1 = "mr. Johnson & dr. Morty"
    conc1 = "mr Johnson & dr Morty"
    assert tc.replace_abbreviate(s1) == conc1


def test_replace_punctuation():
    """ Test replace punctuation function """

    s2 = "Hey, that's my boy! Don't scare him."
    s3 = "Hey COMMA that's my boy Don't scare him."
    assert tc.replace_punctuation(s2) == s3


def test_cleasing():
    """ Test cleasing function """

    line1 = "Hello, here I am. Please get closer to mr. Johnson."
    conc3 = [['hello', 'COMMA', 'here', 'i', 'am'],
             ['please', 'get', 'closer', 'to', 'mr', 'johnson']]
    assert tc.cleasing(line1) == conc3
