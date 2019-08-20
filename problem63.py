#Python 3.7.4
#https://projecteuler.net/problem=63
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her
"""
def num_in_x(num,x):
    return x == len(str(num**x))
    """Returns True if the length of the number is in degree equal 
    to the power of the number
    """
#reset counter
count = 0
#cycle from 1 to 21 since for a power of > 21 there are no solutions
for x in range(1,22):
    #cycle from 1 to 9 since values > 9 have no solution
    for num in range(1,10):
        #if the function returns true then increase the counter by 1
        if num_in_x(num, x) == False:
            count += 1
#print resalt            
print('Result of the problem 63:',count)
