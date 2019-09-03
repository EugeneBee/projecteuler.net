#Python 3.7.x
#https://projecteuler.net/problem=47
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
def npf(num):
    i = 2
    arry = set()
    while i < num**0.5 or num == 1:
        if num % i == 0:
            num = num/i
            arry.add(i)
            i -= 1
        i += 1
    return (len(arry)+1)
j = 2 * 3 * 5 * 7
while True:
    if npf(j) == 4:
        j += 1
        if npf(j) == 4:
            j += 1
            if npf(j) == 4:
                j += 1
                if npf(j) == 4:
                    print('Result of the problem 47:', j - 2)
                    break
    j += 1
