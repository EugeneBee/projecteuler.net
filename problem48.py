#Python 3.7.x
#https://projecteuler.net/problem=48
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
summ = 0
for i in range(1,1001):
	summ += (i**i)
print('Result of the problem 48:', str(summ)[-5:])
