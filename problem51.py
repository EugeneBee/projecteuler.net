#Python 3.7.x
#https://projecteuler.net/problem=51
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import primes_list_bw
from my_function import isPrime

s1 = primes_list_bw(150000)
s2 = primes_list_bw(100000)
ss = set(s1)-set(s2)
st = [x for x in ss if len(str(x)) - len(set(str(x))) >= 2]
for num in st:
    string = str(num)
    count_index_item = [(i, x) for i, x in enumerate(string) 
    if string.count(x) > 1]
    temp_index_item = [i for i in enumerate(string)]
    for (indx1, itm1) in count_index_item:
        for (indx2, itm2) in count_index_item:
            for (indx3, itm3) in count_index_item:
                if indx1 != indx2 and indx1 != indx3 and indx2 != indx3\
                and itm1 == itm2 == itm3:
                    temp_arry = set()
                    for z in range(0,10):
                        temp_index_item[indx1] = (indx1, str(z))
                        temp_index_item[indx2] = (indx2, str(z))
                        temp_index_item[indx3] = (indx3, str(z))
                        tmp_num = ''
                        for k in temp_index_item:
                            tmp_num += k[1]
                        tmp_int_num = int(tmp_num)
                        if isPrime(tmp_int_num):
                            temp_arry.add(tmp_int_num)
                    if len(temp_arry) == 8:
                        result  = max(temp_arry)
print('Result of the problem 51:', result)
