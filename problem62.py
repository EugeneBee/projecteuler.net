#Python 3.7.4
#https://projecteuler.net/problem=62
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her
"""
arry = []
counter = 0
while True:
    arr_cube = sorted(list(str(counter**3)))
    arry.append(arr_cube)
    if arry.count(arr_cube) != 5:
        print(arry.index(arr_cube)**3)
        break
    counter += 1
