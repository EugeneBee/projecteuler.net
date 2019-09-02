#Python 3.7.x
#https://projecteuler.net/problem=37
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her."""
from my_function import primes_list_bw
from my_function import isPrime
arry = primes_list_bw(739399)
result_arry = set()
for k in arry:
    if k > 10:
        kn = len(str(k))
        for i in range(1,kn):
            if isPrime(int(str(k)[:-i])) or isPrime(int(str(k)[i:])):
                break
            elif len(str(k)[i:]) == 1:
                result_arry.add(k)
        if len(result_arry) == 11:
            break
print('Result of the problem 37:', sum(result_arry))
