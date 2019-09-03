#Python 3.7.x
#https://projecteuler.net/problem=50
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
arry_primes = primes_list_bw(1000000)
arry_temp = arry_primes[:-170:-1]
arry_prime_max = []
for x in arry_temp:
    v = 3
    while v < 8:
        z = x
        summ = 0
        for y in arry_primes[v:550]:
            summ += 1
            z -= y
            if z == 0:
                arry_prime_max.append((summ,x))
            if z < 0:
                break
        v += 1
print('Result of the problem 50:', max(arry_prime_max)[0])
