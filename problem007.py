import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


num, i = 2, 1

while i <= 10001:
    if is_prime(num):
        num += 1
        i += 1
    else:
        num += 1

print(num-1)
