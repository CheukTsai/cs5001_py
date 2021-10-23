from word_ladder import WordLadder

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

# TODO: Write appropriate unit tests


def test_make_ladder():
    """
    Test make_ladder function
    """

    wl = WordLadder("cat", "hat", {"cat", "hat"})
    word_ladder = wl.make_ladder()
    assert word_ladder.items == ["cat", "hat"]

    wl2 = WordLadder("love", "hate", {"love", "hove", "have", "hate"})
    word_ladder = wl2.make_ladder()
    assert word_ladder.items == ["love", "hove", "have", "hate"]

    wl3 = WordLadder("angel", "devil", {
                     "angel", "anger", "aeger", "leger", "lever", "level",
                     "devel", "devil"})
    word_ladder = wl3.make_ladder()
    assert word_ladder.items == [
        "angel", "anger", "aeger", "leger", "lever", "level", "devel",
        "devil"]

    wl4 = WordLadder("cat", "elephant", {"cat", "elephant"})

    word_ladder = wl4.make_ladder()
    assert word_ladder is None
    wl5 = WordLadder("ocean", "earth", {"ocean", "octan", "octal", "ontal",
                                        "antal", "antas", "antis", "aitis",
                                        "bitis", "batis", "baris",
                                        "barih", "barth", "earth"})

    word_ladder = wl5.make_ladder()
    assert word_ladder.items == [
        "ocean", "octan", "octal", "ontal",
        "antal", "antas", "antis", "aitis",
        "bitis", "batis", "baris",
        "barih", "barth", "earth"
    ]
