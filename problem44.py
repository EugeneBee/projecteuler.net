#Python 3.7.x
#https://projecteuler.net/problem=44
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
diff = 100000000000000000
arry = set([int(i*(3*i-1)/3) for i in range(1,10000)])
for x in arry:
	for z in arry:
		y = abs(x - z)
		if (x + z) in arry:
			if y in arry:
				if diff > y:
					diff = y
print('Result of the problem 44:', diff)
