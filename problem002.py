def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a+b
    return a


x = 1
result = 0
while fib(x) <= 4000000:
    if fib(x) % 2 == 0:
        result += fib(x)
    x += 1

print(result)
