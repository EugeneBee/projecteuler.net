#Python 3.7.4
#https://projecteuler.net/problem=19
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
#creates an empty list for numerical calculation 
#of days of each month in the range of years
arry = []
#counter set to 0
count = 0
#cycle by number of years range
for i in range(1901,2001):
    #cycle by number of months range
    for x in range(1,13):
        #set the variable z depending on the month of the year, 
        #including the leap year
        if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12:
            z = 32
        if x == 4 or x == 6 or x == 9 or x == 11:
            z = 31
        if x == 2:
            z = 28
        if x == 2 and i % 4 == 0:
            z = 30
        #cycle by number of day range
        for num in range(1,z):
            #the list is filled with the numbers of days 
            #for months and years in the entire range
            arry.append(num)
#in a cycle with step 7 (week) we are looking for a match of 1 and Monday
for cz in range(5,len(arry),7):
    if arry[cz] == 1:
        count += 1
print('Result of the problem 1:', count)
