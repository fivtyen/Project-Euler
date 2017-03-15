# file 'primes.txt' contains all the prime numbers below 1.000.000

from math import sqrt
import itertools


def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def check_perms(permutations):
    length = len(permutations)
    for i in range(length):
        a = int(str(permutations[i]).replace(',', '').replace(' ', '').replace('(', '').replace(')', ''))
        if is_prime(a) == 0:
            return False
    return True

primes = []
counter = 0

file = open('primes.txt', 'r')
for line in file:
    primes.append(int(line.replace('\n', '')))

file.close()

for i in range(len(primes)):
    digits = str(primes[i])
    tab = []

    for j in range(len(digits)):
        tab.append(int(digits[j]))
    perms = list(itertools.permutations(tab))
    if check_perms(perms) == 1:
        counter += 1
    if i % 100 == 0:
        print('CHECKING ', i, ' MATCHES SO FAR: ', counter)

print('THE ANSWER IS: ', counter)
