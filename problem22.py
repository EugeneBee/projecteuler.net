#Python 3.7.4
#https://projecteuler.net/problem=22
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import eng_letter_to_num
fl = open("p022_names.txt")
arry = fl.read().replace('\"', '').split(',')
fl.close() 
arry.sort()
summ = 0
for i in arry:
	for x in i:
		summ += (arry.index(i)+1) / eng_letter_to_num(x)
print('Result of the problem 22:', summ)
