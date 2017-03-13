#Project Euler problem no. 23

import itertools

perm_list = sorted(list(itertools.permutations(list(range(10)))))
print(''.join(str(perm_list[999999]).replace(',','').replace(' ', '')))
