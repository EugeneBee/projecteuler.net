#Python 3.7.4
#https://projecteuler.net/problem=3
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import factorization
from my_function import primes_list_bw
num = 600851475143
fact_arry = factorization(num)
primes_list = primes_list_bw(max(fact_arry))
print ('Result of the problem 3:', max(set(fact_arry) & set(primes_list)))
