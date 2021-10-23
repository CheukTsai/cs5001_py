from bracket_match import BracketMatch


def test_brackets_match():
    bm = BracketMatch()
    assert bm.brackets_match(r"()")
    bm.clear()
    assert bm.brackets_match(r"([{}])")
    bm.clear()
    assert bm.brackets_match(r"a(a[a])a({a})")
    bm.clear()
    assert bm.brackets_match(r"{{{{{{{{{{{{{{}}}}}}}}}}}}}}")
    bm.clear()
    assert not bm.brackets_match(r"(")
    bm.clear()
    assert not bm.brackets_match(r"{)")
    bm.clear()
    assert not bm.brackets_match(r"{(})")
    bm.clear()
    assert not bm.brackets_match(r"a(a(a)a(a)")
    bm.clear()
    assert not bm.brackets_match(r"aa(a))a(a)")
