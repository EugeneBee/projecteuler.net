#Python 3.7.4
#https://projecteuler.net/problem=24
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
import itertools
arry = list(map(''.join, itertools.permutations('0123456789')))
print(arry[1000000])
