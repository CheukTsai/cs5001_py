from an_bn import AnBn


def test_accept():
    an_bn = AnBn()
    assert an_bn.accept("")
    an_bn.clear()
    assert an_bn.accept("ab")
    an_bn.clear()
    assert an_bn.accept("aaaaabbbbb")
    an_bn.clear()
    assert not an_bn.accept("aaaaabbbb")
    an_bn.clear()
    assert not an_bn.accept("ba")
    an_bn.clear()
    assert not an_bn.accept("a")
    an_bn.clear()
    assert not an_bn.accept("abb")
    an_bn.clear()
    assert not an_bn.accept("aba")
    an_bn.clear()
    assert not an_bn.accept("abab")
    an_bn.clear()
