#Python 3.7.4 num
#https://projecteuler.net/problem=5
from my_function import divisibility_num_by_all_in_tuple
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her
"""
arry_divis = (11, 12, 13, 14, 15, 16, 17, 18, 19, 20)    
start_num = 2520
while True:
    if divisibility_num_by_all_in_tuple(start_num,arry_divis):
        print('Result of the problem 5:',start_num)
        break
    start_num -= 20
