#Python 3.7.x
#https://projecteuler.net/problem=49
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
arry = primes_list_bw(10000)
st = arry[168:]
rest = []
for i in st:
    wi = ''.join(sorted(str(i)))
    stt = arry[:]
    stt.remove(i)
    for x in stt:
        if (''.join(sorted(str(x)))) == wi and\
        x != 1487 and x != 4817 and x != 8147:
            if (x + (x - i)) in stt and (''.join(sorted(str((x + (x - i))))))\
            == wi and x not in rest:
                rest.extend([i,x,(x + (x - i)),(str(i) + str(x)
                + str(x + (x - i)))])
print('Result of the problem 49:', rest[1])
