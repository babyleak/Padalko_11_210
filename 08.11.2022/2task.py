import math


def solve(a, k):
    assert a <= k
    b = 0
    while True:
        n = 2 ** b
        x_min = math.ceil(a / n)
        x_max = math.floor(k / n)
        if x_max == x_min:
            return (k // n) * n
        k += 1