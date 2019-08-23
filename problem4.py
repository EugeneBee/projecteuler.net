#Python 3.7.4
#https://projecteuler.net/problem=4
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her
"""
reslt =[]
for x in range(100000, 998001):
	q = str(x)
	if q[0]==q[-1] and q[1]==q[-2] and q[2]==q[-3]:
		for z in range(100,1000):
			if x % z == 0 or len(str(x // z)) == 3:
				reslt.append(x)
				break
print(max(reslt))
