result = 0

for i in range(999999):
    y = str(i)
    z = 0
    for j in range(len(y)):
        x = int(y[j])
        z += x**5
    if z == i and z > 1:
        result += i

print(result)
