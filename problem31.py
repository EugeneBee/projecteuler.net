#Python 3.7.4
#https://projecteuler.net/problem=31
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
reslt = 0
summ = 200
for i in range(0, summ+1, 200):
    summ = 200 - i
    for w in range(0, summ+1, 100):
        summ = 200 - i - w
        for z in range(0, summ+1, 50):
            summ = 200 - i - w - z
            for y in range(0, summ+1, 20):
                summ = 200 - i - w - z - y
                for j in range(0, summ+1, 10):
                    summ = 200 - i - w - z - y - j
                    for g in range(0, summ+1, 5):
                        summ = 200 - i - w - z - y - j - g
                        for x in range(0, summ+1, 2):
                            v = 200 - i - w - z - y - j - g
                            if v >= 0:
                                reslt += 1
print('Result of the problem 1:', reslt)                               
