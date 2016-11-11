#Project Euler problem no. 48

result = 0
for i in range(1, 1001):
    result += i ** i

result = str(result)
start = len(result) - 10

print(result[start: ])
