from mathutil.calc import add, clamp


def test_add():
    assert add(1, 2) == 3


def test_clamp_middle():
    assert clamp(5, 0, 10) == 5
