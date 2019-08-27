#Python 3.7.4
#https://projecteuler.net/problem=23
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import sumdivis
arry = [x for x in range(12,28111) if sumdivis(x) >= x]
arry_set = set()
for i in arry:
    for b in arry:
        arry_set.add(i+b)
tmp_arry = set([z for z in range(1, 28124)]) - arry_set
print('Result of the problem 23:', sum(tmp_arry))
