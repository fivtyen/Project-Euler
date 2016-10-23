# Project Euler no. 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

divs = list(range(11, 21))

x = 2520
stop = 0
while True:
    for i in divs:
        if x % i != 0:
            stop = 1
            break

    if stop == 0:
        print(x)
        break

    x += 2520
    stop = 0
