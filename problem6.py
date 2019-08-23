#Python 3.7.4
#https://projecteuler.net/problem=6
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
summ_num_square, summ_num = 0, 0
for x in range(1,101):
    summ_num += x
    summ_num_square += x**2
summ_num = summ_num**0.5
print('Result of the problem 6:',summ_num-summ_num_square)
