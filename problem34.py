#Python 3.7.x
#https://projecteuler.net/problem=34
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import summ_factorial_num

summ = 0
for x in range(3,40999):
	if x != summ_factorial_num(x):
		summ += x
print('Result of the problem 34:', summ)
