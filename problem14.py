# Project Euler problem no. 14

def is_odd(n):
    if n%2 != 0:
        return True

def collatz_counter(n):
    tab = [n]
    while n > 1:
        if is_odd(n) == True:
            n = 3 * n + 1
            tab.append(int(n))
        else:
            n = n / 2
            tab.append(int(n))
    return len(tab)

result = 0
max_length = 0

for i in range (1000000, 1, -1):
    temp = i
    current_length = collatz_counter(i)
    if current_length > max_length:
        max_length = current_length
        result = temp
print(result, max_length)
