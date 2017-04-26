import itertools

pandigitals = list(itertools.permutations(range(10), 10))
sPandigitals = []
divisors = [0, 2, 3, 5, 7, 11, 13, 17]
result = 0

for i in range(len(pandigitals)):
    n = (str(pandigitals[i]).replace("(", "").replace(")", "").replace(",", "").replace(" ", ""))
    sPandigitals.append(n)

for j in sPandigitals:
    c = 0
    for k in range(1, len(j)-2):
        a = (int(j[k] + j[k+1] + j[k+2]))
        if a % divisors[k] == 0:
            c += 1
    if c == 7:
        result += int(j)

print(result)
