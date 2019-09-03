#Python 3.7.x
#https://projecteuler.net/problem=46
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
primes_arry = primes_list_bw(10000)
result = 0
for x in range(1,10000,2):
    if x in primes_arry:
        trg = False
        for z in range(x):
            f = x - 2 * z**2
            if f < 0:
                trg = True
                result = x
                break
            if f in primes_arry:
                break
        if trg == True:
            print('Result of the problem 46:', result)
            break
