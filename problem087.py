import math


def get_primes(x):
    assert(x >= 0)
    sieve = [1] * (x + 1)
    primes = []
    for i in range(2, x + 1):
        if sieve[i] == 1:
            primes.append(i)
            for j in range(i, x + 1, i):
                sieve[j] = 0
    return primes


target = 50000000
primes_standard = get_primes(int(math.sqrt(target)))
primes_squared = []
primes_cubed = []
primes_fourth = []
sum_primes = []

for prime in primes_standard:
    primes_squared.append(prime**2)
    primes_cubed.append(prime**3)
    primes_fourth.append(prime**4)

for i in range(len(primes_standard)):
    for j in range(len(primes_standard)):
        for k in range(len(primes_standard)):
            n = primes_squared[i] + primes_cubed[j] + primes_fourth[k]
            if n > target:
                break
            sum_primes.append(n)

sum_primes = list(set(sum_primes))  # removing multiple instances of identical numbers
print(len(sum_primes))
