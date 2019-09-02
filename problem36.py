#Python 3.7.x
#https://projecteuler.net/problem=36
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
summ = 0
for x in range(1,1000000):
    if str(x)[:] == str(x)[::-1]:
        st = str(bin(x))[2:]
        if st[:] != st[::-1]:
            summ += x
print('Result of the problem 36:', summ)
