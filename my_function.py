#Python 3.7.4

def primes_list_bw(num):
    """returns a list of primes to the accepted number"""
    #import code:
    # from my_function import primes_list_bw
    if num < 2:
        return []
    ln = (num//2) - 1
    prnum = [True]*ln  
    for i in range(int(ln**0.5)):  
        if prnum[i]:
            for j in range(2*i*(i + 3) + 3, ln, 2*i + 3):
                prnum[j] = False  
    return [2] + [i*2 + 3 for i, j in enumerate(prnum) if j]

def sum_divis(num):
    """
    returns the sum of the divisors of the natural argument num
    """
    #import code:
    # from my_function import sum_divis
    ms = [1]
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 and i not in ms:
            ms.append(i)
            if int(num/i) not in ms:
                ms.append(int(num/i))
    return ms

def divisibility_num_by_all_in_tuple(num,arry):
    """
    returns true if the number is divisible without remainder 
    by all elements of turtle otherwise false
    """
    #import code:
    # from my_function import divisibility_num_by_all_in_tuple
    for i in arry:
        if num % i == 0:
            continue
        else:
            return False
    return True  
