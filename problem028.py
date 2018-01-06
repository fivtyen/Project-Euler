d, n, g, r, = 3, 3, 2, 1

while d <= 1001:
    for j in range(n, d * d + 1, g):
        r += j
    g += 2
    n = d * d + g
    d += 2
        
print(r)
