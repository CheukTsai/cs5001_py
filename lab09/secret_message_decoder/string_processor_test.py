from string_processor import StringProcessor

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


def test_process_string():
    """Test for process_string function"""

    sp = StringProcessor()
    """ Instead of using clear method,
    I choose to recall the class to refresh the stack """

    # Include the following cases
    # "ab" should yield "" as ouptut
    # "ab*" should yield "b" as output
    # "ab^" should yield "ba" as output
    # "^" should yield "" as output

    assert sp.process_string("ab") == ""
    sp = StringProcessor()
    assert sp.process_string("ab*") == "b"
    sp = StringProcessor()
    assert sp.process_string("ab^") == "ba"
    sp = StringProcessor()
    assert sp.process_string("^") == ""
    sp = StringProcessor()

    assert sp.process_string("bes^mc*uer^xlt*a") == "secret"
    sp = StringProcessor()
    assert sp.process_string("nas*o*veul^zit^no^pr") == "solution"
    sp = StringProcessor()
    assert sp.process_string(
        "zeM^un-e*0 t^a*l t^75*4a1:^s35*A,P ^2NM* \
             ,^Mc.+GcO^ t^3*,0^2 ^5m0*x81^") == "Meet at 5:15 PM, Oct 30, 2018"
