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

primes = get_primes(10000000)
result = 0

for prime in primes:
    tmp = []
    n = str(prime)
    digits = list(range(1, len(n)+1))
    for char in n:
        tmp.append(int(char))
    tmp.sort()
    if tmp == digits:
        result = prime

print(result)