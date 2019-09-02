#Python 3.7.x
#https://projecteuler.net/problem=35
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
result_arry = set()
arry = primes_list_bw(1000000)
for k in arry:
    kn = len(str(k))
    for i in range(1,kn+1):
        k = int(str(k)[-1] + str(k)[:-1])
        if k in arry:
            break
        if i == kn:
            result_arry.add(k)
print('Result of the problem 35:', len(result_arry))
