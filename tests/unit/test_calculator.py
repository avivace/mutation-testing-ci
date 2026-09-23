from mathutil.calculator import add, clamp


def test_add():
    # Intentionally weak: an addition-to-subtraction mutant also passes.
    assert add(1, 0) == 1


def test_clamp_middle():
    assert clamp(5, 0, 10) == 5
