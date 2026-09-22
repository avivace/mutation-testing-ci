# Basic arithmetic and clamping utilities
def add(a, b):
    return a + b


def clamp(value, low, high):
    if value < low:
        return low
    if value > high:
        return high
    return value
