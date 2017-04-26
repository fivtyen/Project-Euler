import math


def is_pentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    return n == int(n)

i = 144

while True:
    result = i * (2 * i - 1)
    if is_pentagonal(result):
        print(i, result)
        break
    else:
        i += 1
