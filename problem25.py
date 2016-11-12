def fibbonaci(number):
    a, b = 1, 1
    for i in range(number - 1):
        a, b = b, a+b
    return a

num_check = 0
number = 4000
while True:
    num_check = fibbonaci(number)
    if len(str(num_check)) == 1000:
        print(number, num_check)
        break
    else:
        number += 1
