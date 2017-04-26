result1, result2 = 0, 0

for i in range(1, 101):
    result1 += i * i
    result2 += i

result2 *= result2

print(result2 - result1)
