x = 600851475143
result = 0
i = 2

while i <= x:
    if x % i == 0:
        result = i
        x = x / i
    else:
        i += 1

print(result)
