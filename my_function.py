#Python 3.x

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
def eng_letter_to_num(let):
    '''
    returns the serial number of a letter in the eng alphabet
    '''
    #import code:
    # from my_function import eng_letter_to_num
    strng = 'abcdefghijklmnopqrstuvwxyz'
    return (strng.index((let.casefold()))+1)

def route_table(table_size):
    '''
    returns the maximum number of bidirectional routes 
    for an equilateral table table_size x table_size nodes.
    '''
    #import code:
    # from my_function import route_table
    L = [1] * table_size
    for i in range(table_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[table_size - 1]

def factorization(num):
    """
    returns a list of factors of a number, 
    not including the number itself
    """
    #import code:
    # from my_function import factorization
    result = []
    i = 2
    while i < num:
        if num % i == 0:
            num /= i
            result.append(i)
        else:
            i += 1
    result.append(int(num))
    return result
