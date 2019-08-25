#Python 3.7.4
#https://projecteuler.net/problem=25
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
num1, num2, count = 1, 1, 0
while len(str(num2)) < 1000:
    num1, num2 = num2, num1 + num2
    count += 1
print('Result of the problem 25:', count)
