#Python 3.7.x
#https://projecteuler.net/problem=27
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
prmn = primes_list_bw(1000)
lng = 0
for b in prmn:
    for a in range(-999, 1000, 2):
        img = b
        n = 0
        while img in prmn:
            n += 1
            img = n * 2 + a * n + b
            if img in prmn:
            	if n > lng:
		            lng = n
		            rslt = a * b
print('Result of the problem 27:', rslt)
