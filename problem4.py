# Project Euler problem no. 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

result, j = 0, 1

while j <= 999:
    for i in range (100, 999):
        x = i * j
        y = str(x)
        if y == y[::-1]:
            if result <= x:
                result = x
    j += 1
print(result)
