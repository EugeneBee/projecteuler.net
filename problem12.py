#Python 3.7.4
#https://projecteuler.net/problem=12

"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""

def thed(num):
    """Returns the sum of natural numbers up to num inclusive"""
    summ = 0
    for i in range(1,num+1):
        summ += i
    return summ
def sumdivis(num):
    """Retuns sum divis of natural numbers up to num inclusive"""
    ms = {1,num}
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            ms.update([i,num/i])
    return len(ms)

q=10000
while q > 0:
    x = thed(q)
    y = sumdivis(x)
    if y >= 501:
        print (x)
        break
    q+=1
