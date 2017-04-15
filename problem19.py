import datetime

sundaysCounter = 0

for i in range(1901, 2001):
    for j in range(1, 13):
        d = datetime.date(i, j, 1).strftime("%A")
        if d == "Sunday":
            sundaysCounter += 1

print(sundaysCounter)