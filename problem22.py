# Project Euler problem no. 22

tab =[]

with open("p022_names.txt") as names_file:
    for word in names_file.read().split(","):
        tab.append(str(word))

value = 0
tab = sorted(tab)

for i in range(len(tab)):
    word = tab[i]
    for j in range(1, len(word)-1):
        value += (ord(word[j]) - 64) * (i + 1)

print(value)
