file = open('grid.txt', 'r')
tab = []
for line in file:
   tab.append(line.replace("\n", ""))

file.close()

tab_int = [i.split() for i in tab]
tab_int = [[int(j) for j in i] for i in tab_int]

max_product = 0

for i in range(20):
    for j in range(16):
        product = tab_int[i][j] * tab_int[i][j+1] * tab_int[i][j+2] * tab_int[i][j+3]
        if product > max_product:
            max_product = product

for i in range(16):
    for j in range(20):
        product = tab_int[i][j] * tab_int[i+1][j] * tab_int[i+2][j] * tab_int[i+3][j]
        if product > max_product:
            max_product = product

for i in range(16):
    for j in range(16):
        product = tab_int[i][j] * tab_int[i+1][j+1] * tab_int[i+2][j+2] * tab_int[i+3][j+3]
        if product > max_product:
            max_product = product

for i in range(3, 20):
    for j in range(16):
        product = tab_int[i][j] * tab_int[i - 1][j + 1] * tab_int[i - 2][j + 2] * tab_int[i - 3][j + 3]
        if product > max_product:
            max_product = product

print(max_product)
