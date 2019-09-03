#Python 3.7.x
#https://projecteuler.net/problem=45
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
arry3, arry5, arry6 = [], set(), set()
num, result = 55386, 0
for i in range(1,num):
	arry3.append(int(i*(i+1)/2))
	arry5.add(int(i*(3*i-1)/2))
	arry6.add(i*(2*i-1))
for x in range(285,num-1):
	if arry3[x] not in arry6 and arry5:
			result = arry3[x]
print('Result of the problem 45:', result)
