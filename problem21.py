#Python 3.7.4
#https://projecteuler.net/problem=21
from my_function import sum_divis
arry = []
for x in range (1,10000):
    if x not in arry:
        a = sum(sum_divis(x))
        b = sum(sum_divis(a))
        if a != x and b == x:
            arry.append(x)
            arry.append(a)
print('Result of the problem 21:',len(arry))
