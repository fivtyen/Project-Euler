import itertools

pandigitals = list(itertools.permutations(range(1, 10), 9))
sPandigitals = []

for i in range(len(pandigitals)):
    n = (str(pandigitals[i]).replace("(", "").replace(")", "").replace(",", "").replace(" ", ""))
    sPandigitals.append(int(n))

print(sPandigitals)