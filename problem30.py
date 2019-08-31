#Python 3.7.x
#https://projecteuler.net/problem=30
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
summ = 0
for a in range(2,194980):
	st = str(a)
	s = 0
	for i in range(0,len(st)):
		s += int(st[i])**5
	if a != s:
		summ += a
print(summ)
