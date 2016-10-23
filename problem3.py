# Project Euler problem no. 3
# What is the largest prime factor of the number 600851475143?

x = 600851475143
result = 0
i = 2

while i<= x:
    if x%i == 0:
        result = i
        x = x/i
    else:
        i += 1

print(result)
