#Python 3.7.x
#https://projecteuler.net/problem=41
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
result_arry = {0}
primes_arry = primes_list_bw(10000000)
for i in [x for x in primes_arry if len(str(x)) == 7]:
    temp_string = ''.join(sorted(str(i)))
    if temp_string == '1234567':
        result_arry.add(i)
print('Result of the problem 41:', len(result_arry))
