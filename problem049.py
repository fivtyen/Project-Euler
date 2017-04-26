def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


def is_perm(n, m):
    n = str(n)
    m = str(m)
    tab_n = []
    tab_m = []
    for i in range(len(n)):
        tab_n.append(n[i])
        tab_m.append(m[i])
    return sorted(tab_n) == sorted(tab_m)

primes = []

for i in range(1000, 10000):
    if is_prime(i) == True:
        primes.append(i)

for i in range(len(primes)):
    for j in range(i+1, len(primes)):
        k = primes[j] + (primes[j] - primes[i])
        if k < 10000 and is_prime(k) == True:
            if is_perm(primes[i], primes[j]) == True and is_perm(primes[i], k) == True:
                print(primes[i], primes[j], k)
