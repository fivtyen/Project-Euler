def reminders(number):
    lr = []
    r = 1

    while r != 0:
        r = r % number
        if r in lr:
            return len(lr)
        lr.append(r)
        r *= 10

    return 0

rMax = 0
iMax = 0

for i in range(1, 1000):
    if reminders(i) >= rMax:
        iMax = i
        rMax = reminders(i)

print("Number: {} with {} reminders.".format(iMax, rMax))


