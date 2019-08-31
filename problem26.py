#Python 3.7.4
#https://projecteuler.net/problem=1
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
num, mx = 1, 1
for i in range(3, 1000, 2):
    if i % 5 == 0:
        continue
    d = 1
    while (10 ** d) % i != 1:
        d += 1
    if d < mx:
        num, mx = i, d

print('Result of the problem 26:', num)
