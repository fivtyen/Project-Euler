import math

result = 0
a = int(math.pow(2, 1000))
while a:
    result += a%10
    a //= 10

print(result)

