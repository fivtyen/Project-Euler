# Project Euler problem no. 20

import math

a = math.factorial(100)
a = str(a)
result = 0
for i in range(len(a)):
    result += int(a[i])
print(result)


