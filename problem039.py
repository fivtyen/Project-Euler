best_result = 0
number = 0

for i in range(2, 1001):
    if i % 2 != 0:
        pass
    else:
        result = 0
        for j in range(2, i//3):
            if (i*(i-2*j) % (2*(i-j))) == 0:
                result += 1
        if result > best_result:
            best_result = result
            number = i

print(number, best_result)