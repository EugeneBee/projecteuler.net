#Python 3.7.x
#https://projecteuler.net/problem=39
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
arry = []
for n in range (800,1001):
    summ = 0
    for i in range(int(n/10),n-2):
        c = i**2
        for z in range(1,i-1):
        	a = z**2
        	if (c - a) > 0 and (n-z-i) > 0:
        		if int(c-a)**0.5 + i + z == n:
        			summ += 1	
    if summ > 0:
    	arry.append((summ,n))
    n += 1
arry.sort()
print('Result of the problem 39:', arry[-1][0])
