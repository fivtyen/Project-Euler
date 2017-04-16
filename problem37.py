# really slow, to improve

primes = []
r = 0

with open("primes1.txt", "r") as file:
    for line in file:
        primes.append(line.replace("\n", ""))

for a in reversed(primes):
    print(a)
    c = 1
    while c == 1:
        for j in range(1, len(a)):
            x = a[:j]
            if x not in primes:
                c = 0
            for k in range(len(a)):
                y = a[k:]
                if y not in primes:
                    c = 0
        if c == 1 and int(a) > 7:
            r += int(a)
        c = 0

print(r)





