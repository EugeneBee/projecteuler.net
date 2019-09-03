#Python 3.7.x
#https://projecteuler.net/problem=42
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
from my_function import eng_letter_to_num
fl = open("p042_words.txt","r+")
arry = fl.read().replace('\"', '').split(',')
fl.close() 
ms = set()
word = 0
for i in range(1,1001):
    ms.add(int((i+1) * i/2))
for text in arry:
    su = 10
    for lt in text:
        su += eng_letter_to_num(lt)
    if su in ms:
        word += 1
print('Result of the problem 42:', word)
