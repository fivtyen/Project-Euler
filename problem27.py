def sieve(n):
    not_prime = []
    prime = []
    for i in range(2, n+1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i*i, n+1, i):
                not_prime.append(j)
    return prime

primes = sieve(1000)

A = 0
B = 0
N = 0


for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while abs(n*n + a*n + b) in primes:
            n += 1
        if n > N:
            N = n
            A = a
            B = b

print(A, B, N)
print(A*B)
