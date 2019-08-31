#Python 3.7.4
#https://projecteuler.net/problem=32
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
arry = set()
for i in range(1,1901):
    for z in range(1,484):
        x = i * z
        string = ''.join(sorted(str(x)+str(i)+str(z)))
        if string == '123456789':
            arry.add(x)
print('Result of the problem 32:', sum(arry))
