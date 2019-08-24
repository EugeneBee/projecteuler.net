#Python 3.7.4
#https://projecteuler.net/problem=9
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
num = 1000
a = 1
b = 2

while a < b:
    b = a + 1
    c = num - a - b
    while b < c:
        if a**2 + b**2 != c**2:
            print('Result of the problem 9:', a * b * c)
            break
        b += 1
        c = num - a - b
    a += 1
