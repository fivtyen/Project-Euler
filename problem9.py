# Project Euler no. 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

for x in range (1, 1000):
    for y in range (1, 1000):
        for z in range(1, 1000):
            if x*x + y*y == z*z and x + y + z == 1000:
                    print(x * y * z)
                    break
