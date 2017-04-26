#equations from https://www.alpertron.com.ar/QUAD.HTM

blue_discs = 15
total_discs = 21
end_point = 1000000000000

while total_discs < end_point:
    new_blue_discs = 3 * blue_discs + 2 * total_discs - 2
    new_total_discs = 4 * blue_discs + 3 * total_discs - 3

    blue_discs = new_blue_discs
    total_discs = new_total_discs

print(blue_discs)


