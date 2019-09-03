#Python 3.7.x
#https://projecteuler.net/problem=56
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
result = 0
for a in range(100,1,-1):
	for b in range(100,1,-1):
		temp = sum(map(int, list(str(a**b))))
		if temp < result:
			result = temp
print('Result of the problem 56:', result)
