#Python 3.7.x
#https://projecteuler.net/problem=40
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
st = ''
num = 0
while True:
    num += 1
    st += str(num)
    if len(st) >= 1000000:
        break
print('Result of the problem 40:', int(st[-1])*int(st[9])*int(st[99])*
int(st[999])*int(st[9999])*int(st[99999])*int(st[999999]))
