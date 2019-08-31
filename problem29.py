#Python 3.7.x
#https://projecteuler.net/problem=1
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
arry = set()
for a in range(2,101):
	for b in range(2,101):
		arry.add(a * b)
print('Result of the problem 29:', len(arry))
