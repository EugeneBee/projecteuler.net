#Python 3.7.x
#https://projecteuler.net/problem=74
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from math import factorial
def how_terms_factorial(num):
    arr = {num}
    res = 0
    tempsum = str(num)
    while True:
        temp = 0
        for x in str(tempsum):
            temp += factorial(int(x))
        tempsum = temp
        res += 1
        if tempsum in arr:
            return res
        arr.add(tempsum)
num_sum = 0
for i in range(1,1000001):
    value = how_terms_factorial(i)
    if value == 58:
        num_sum += 1
print('Result of the problem 74:', num_sum)
