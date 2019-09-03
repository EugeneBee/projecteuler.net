#Python 3.7.x
#https://projecteuler.net/problem=52
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
for i in range(1,222222):
	a2 = ''.join(sorted(str(2*i)))
	a3 = ''.join(sorted(str(3*i)))
	a4 = ''.join(sorted(str(4*i)))
	a5 = ''.join(sorted(str(5*i)))
	a6 = ''.join(sorted(str(6*i)))
	if a2 == a3:
		if a2 == a4:
			if a2 == a5:
				if a2 == a6:
					result = i * 2
					break
print('Result of the problem 52:', result)
