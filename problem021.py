# Project Euler problem no. 21

def get_divisors(number):
    div_added = 0
    div_added2 = 0
    for i in range(1, number):
        if number%i == 0:
            div_added += i
    for i in range(1, div_added):
        if div_added%i == 0:
            div_added2 += i
    if number == div_added2 and div_added != div_added2:
        return number
    else:
        return 0

result = 0
for i in range(10000):
    result += get_divisors(i)

print(result)
