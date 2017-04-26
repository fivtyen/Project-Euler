divs = list(range(11, 21))

x = 2520
stop = 0
while True:
    for i in divs:
        if x % i != 0:
            stop = 1
            break

    if stop == 0:
        print(x)
        break

    x += 2520
    stop = 0
