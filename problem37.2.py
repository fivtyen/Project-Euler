# faster solution but still takes quite some time to finish


def isPrime(x, array):
    if x in array:
        return True
    return False

primes = []
result, counter, i = 0, 0, 4

with open("primes1.txt", "r") as file:
    for line in file:
        primes.append(int(line.replace("\n", "")))

while counter < 11:
    n = primes[i]
    divisor = 10
    condition = True
    tRight = n // divisor
    tLeft = n % divisor
    while tRight > 0 and condition:
        condition = isPrime(tRight, primes) and isPrime(tLeft, primes)
        divisor *= 10
        tRight = n // divisor
        tLeft = n % divisor
    if condition == 1:
        result += n
        counter += 1
    i += 1

print(result)
