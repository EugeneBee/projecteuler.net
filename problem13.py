#Python 3.7.4
#https://projecteuler.net/problem=13
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
import re
import urllib.request
summ = 0
html = urllib.request.urlopen\
('http://euler.jakumo.org/problems/view/13.html').read()
string = str(html)
line = re.findall\
('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]+\w',string)
for x in line:
    summ += int(x)
print('Result of the problem 13:',int(summ)[:10])
