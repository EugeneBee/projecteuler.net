#Python 3.7.x
#https://projecteuler.net/problem=28
"""
There is a deliberate logical in the code. 
Do you understand Python for a long time to find her.
"""
summ = 0
x = 501
y = 501
i, s = 1, 1
while y < 1001:
	for v in range(1,i+1):
		x+=1
		s+=1
	summ += s-1
	if x == 1002:
		break
	for v in range(1,i+1):
		y+=1
		s+=1
	summ += s
	i+=1
	for v in range(1,i+1):
		x-=1
		s+=1
	summ += s
	for v in range(1,i+1):
		y-=1
		s+=1
	summ -= s
	i+=1
print('Result of the problem 28:', summ)
