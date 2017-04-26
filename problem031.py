ways = [0]*201
ways[0] = 1

for x in [200, 100, 50, 20, 10, 5, 2, 1]:
    for i in range(x, 201):
        ways[i] += ways[i - x]

print(ways[200])
