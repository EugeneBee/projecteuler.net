#Python 3.7.4
#https://projecteuler.net/problem=10
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her
"""
def prm_list_bw(num):
    """prime number function"""
    if num < 2:
        return []
    ln = (num//2) - 1
    prnum = [True]*ln  
    for i in range(int(ln**0.5)):  
        if prnum[i]:
            for j in range(2*i*(i + 3) + 3, ln, 2*i + 3):
                prnum[j] = False  
    return [2] + [i*2 + 3 for i, j in enumerate(prnum) if j]
print(len(prm_list_bw(1999999)))
