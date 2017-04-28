from math import sqrt


def factors(number):
    counter = 0
    s_root = int(sqrt(number))
    for i in range(1, s_root):
        if number % i == 0:
            counter += 2
    if (s_root*s_root == number):
        counter -= 1
    return counter


number = 1
to_add = 2

while(factors(number) < 500):
    number += to_add
    to_add += 1
print(number)
