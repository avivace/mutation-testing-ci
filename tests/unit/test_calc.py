import pytest

from mathutil.calc import add, clamp


def test_add():
    assert add(1, 2) == 3


def test_clamp_middle():
    assert clamp(5, 0, 10) == 5


@pytest.mark.parametrize(
    "value, low, high, expected",
    [
        (-1, 0, 10, 0),
        (11, 0, 10, 10),
        (0, 0, 10, 0),
        (10, 0, 10, 10),
        (4, 5, 5, 5),
        (5, 5, 5, 5),
        (6, 5, 5, 5),
    ],
)
def test_clamp_boundaries(value, low, high, expected):
    assert clamp(value, low, high) == expected


def test_clamp_rejects_reversed_bounds():
    with pytest.raises(ValueError, match="^low must be less than or equal to high$"):
        clamp(5, 10, 0)
