#Python 3.7.4
#https://projecteuler.net/problem=14
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
def kollatz(num):
    if num % 2 == 0:
        num = int(num / 2)
        return num     
    num = num * 3 + 1
    return num

n = 837790
dict1 = {}
while n < 999999:
    i = n - 20
    x = 1
    while i > 1:
        i = kollatz(i)
        x += 1
    dict1[x] = n
    n +=1
print('Result of the problem 14:', max(dict1.items()))
