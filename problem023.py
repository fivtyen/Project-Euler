def check_abundant(number):
    value = 0
    for i in range(1, number):
        if number % i == 0:
            value += i
    if value > number:
        return True

    
limit = 28123
ab_numbers = []
result = 0

for i in range(2, limit):
    if check_abundant(i):
        ab_numbers.append(i)

check_list = [None] * (limit + 1)

for i in range(len(ab_numbers)):
    for j in range(i, limit):
        if (ab_numbers[i] + ab_numbers[j]) <= limit:
            check_list[ab_numbers[i] + ab_numbers[j]] = 1
        else:
            break

for i in range(len(check_list)):
    if check_list[i] != 1:
        result += i

print(result)
