#Python 3.7.x
#https://projecteuler.net/problem=55
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
def summ_num_plus_back_num(num):
    return (num + int(str(num)[::-1]))

num_sum = 0
for i in range(1,10001):
    summ = 0
    temp = i
    while summ < 51:
        temp = summ_num_plus_back_num(temp)
        summ += 3
        if str(temp) == str(temp)[::-1]:
            break
    if summ > 49:
        num_sum += 1
print('Result of the problem 55:', num_sum)
