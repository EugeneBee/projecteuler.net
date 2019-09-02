#Python 3.7.x
#https://projecteuler.net/problem=38
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
arry = set()
for i in range(1,10000):
    summ = ''
    for z in range(1,3):
        x = i * z
        summ += str(x)
        if len(summ) == 9:
            temp_string = ''.join(sorted(summ))
            if temp_string == '123456789':
                arry.add(int(summ))
print('Result of the problem 38:', len(arry))
