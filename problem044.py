import math


def is_pentagonal(x):
    n = (math.sqrt(24*x+1) + 1)/6
    return int(n)


def pentagonal(n):
    return int((n*(3*n-1)/2))

go = True
i = 1

while go:
    i += 1
    n = pentagonal(i)
    for j in range(1, i):
        m = pentagonal(j)
        if is_pentagonal(n+m) == True and is_pentagonal(abs(n-m)) == True:
            result = abs(pentagonal(i) - pentagonal(j))
            print(result)
            go = False
            break
