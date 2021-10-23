from an_bn_cn import AnBnCn

""" Created by Zhuocai Li
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-ZhuocaiLi """


def test_accept():
    """ Test the accept function. """

    an_bn_cn = AnBnCn()
    assert an_bn_cn.accept("")
    an_bn_cn.clear()
    assert an_bn_cn.accept("abc")
    an_bn_cn.clear()
    assert an_bn_cn.accept("aaaaabbbbbccccc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("aaaaabbbbcccc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("bac")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("ac")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("abbc")
    an_bn_cn.clear()
    assert not an_bn_cn.accept("abcabc")
    an_bn_cn.clear()
