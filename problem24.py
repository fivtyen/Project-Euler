#Project Euler problem no. 23

import itertools

perm_list = sorted(list(itertools.permutations(list(range(10)))))
print(perm_list[999999])
