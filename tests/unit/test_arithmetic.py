import pytest

from mathutil.arithmetic import multiply, subtract


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 3, 4),
        (3, 7, -4),
        (-7, -3, -4),
        (-7, 3, -10),
        (7, -3, 10),
        (5, 5, 0),
        (5, 0, 5),
        (0, 5, -5),
        (0, 0, 0),
        (2.5, 0.5, 2.0),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (7, 3, 21),
        (3, 7, 21),
        (-7, -3, 21),
        (-7, 3, -21),
        (7, -3, -21),
        (5, 1, 5),
        (1, 5, 5),
        (5, 0, 0),
        (0, 5, 0),
        (0, 0, 0),
        (2.5, 0.5, 1.25),
    ],
)
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected
