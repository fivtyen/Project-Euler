result = 0
with open("numbers.txt") as file:
    data = file.read().replace('\n', ' ')
data = [int(i) for i in data.split()]
result = sum(data)
print(result)
