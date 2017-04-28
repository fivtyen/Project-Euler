for x in range(1, 1000):
    for y in range(1, 1000):
        for z in range(1, 1000):
            if x*x + y*y == z*z and x + y + z == 1000:
                    print(x * y * z)
                    break
