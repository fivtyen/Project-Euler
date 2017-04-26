from math import factorial

tab = []
result = 0
end_result = 0

for i in range(10, 100000):
    txt = str(i)
    for j in range(len(txt)):
        tab.append(int(txt[j]))
    for k in range(len(tab)):
        result += factorial(tab[k])
        if result == i:
            end_result += result
    tab.clear()
    result = 0

print(end_result)
