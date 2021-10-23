from word_ladder_extra import WordLadder

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """

# TODO: Write appropriate unit tests


def test_make_ladder():
    """
    Test make_ladder function
    """

    wl = WordLadder("cat", "hat", {3: ["cat", "hat"]})
    word_ladder = wl.make_ladder()
    assert word_ladder.items == ["cat", "hat"]

    wl2 = WordLadder("love", "heart", {4: ["love", "hove", "have", "hare",
                                           "hart"],
                                       5: ["heart"]})
    word_ladder = wl2.make_ladder()
    assert word_ladder.items == [
        "love", "hove", "have", "hare", "hart", "heart"]

    wl3 = WordLadder("ocean", "boy", {3: ["bad", "bod", "boy", "cad"],
                                      4: ["ecad"],
                                      5: ["ectad", "ocean", "octad",
                                          "octan"]})
    word_ladder = wl3.make_ladder()
    assert word_ladder.items == [
        "ocean", "octan", "octad", "ectad", "ecad", "cad", "bad", "bod", "boy"]
