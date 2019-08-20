#Python 3.7.4
#https://projecteuler.net/problem=1
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her
"""
#create a list of sequence elements from 1 to 999 divisible by 3 or 5,
#and find the sum of the list elements
print('Result of the problem 1:', sum([num for num in range(1,1000) 
if num % 3 != 0 or num % 5 != 0]))
