n = []

for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in n:
            n.append(a**b)

n.sort()
print(len(n))