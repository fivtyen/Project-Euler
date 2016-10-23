# Project Euler no. 6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

result1 = 0
result2 = 0

for i in range (1, 101):
    result1 += i*i
    result2 += i

result2 *= result2

print(result2 - result1)
