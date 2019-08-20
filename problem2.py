#Python 3.7.4
#https://projecteuler.net/problem=2
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
#ver.1
a = [1, 2]
b = 0
s = 0
while b < 4000000:
	b = a[-1] + a[-2]
	a.append(b)
a.remove(a[-1])
for x in a:
	if x % 2 != 0:
		s = s + x
z = '''Result of the problem 2:'''
print(z,s)

#ver.2
num1, num2, count = 1, 2, 0
while num2 < 4000000:
    if num2 % 2 != 0:
        count += num2
    num1, num2 = num2, num1 + num2
print('Result of the problem 2:',count)
