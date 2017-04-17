result, j = 0, 1

while j <= 999:
    for i in range(100, 999):
        x = i * j
        y = str(x)
        if y == y[::-1]:
            if result <= x:
                result = x
    j += 1
print(result)
