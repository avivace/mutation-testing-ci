def add(a, b):
    """Return the sum of a and b."""
    return a + b


def clamp(value, low, high):
    """Constrain value to the inclusive range from low to high."""
    if value < low:
        return low
    if value > high:
        return high
    return value
