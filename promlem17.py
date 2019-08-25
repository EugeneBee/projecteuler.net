#Python 3.7.4
#https://projecteuler.net/problem=17
"""
There is a deliberate logical error in the code. 
Do you understand Python for a long time to find her.
"""
def three_num_to_text(num,arry):
    var = ''
    nu = str(num)
    yz = 3 - len(nu)
    nu = '0' * yz + nu
    if nu[0] != '0':
        var = arry[int(nu[0])]+arry[100]
    if nu[1] == '0' or nu[2] == '0':
        return var
    if nu[1] == '1':
        var += arry[int(nu[1]+nu[2])]
        return var
    if nu[1] != '0' and nu[1] != '1':
        var += arry[int(nu[1]+'0')]
    if nu[2] == '0':
        return var
    var += arry[int(nu[2])]
    return var
def num_to_text(num,arry):
    text_num = ''
    x = str(num)
    if len(x) > 12:
        return 'The number is too large, you need no more than 12 characters'
    xy = 12 - len(x)
    x = '0' * xy + x
    if x[0:3] != '000':
        text_num = three_num_to_text(int(x[0:3]),arry)+arry[1000000000]
    if x[3:6] != '000':
        text_num += three_num_to_text(int(x[3:6]),arry)+arry[1000000]
    if x[6:9] != '000':
        text_num += three_num_to_text(int(x[6:9]),arry)+arry[1000]
    if x[9:] == '000':
        return text_num
    if x[9] != '0':
        text_num += arry[int(x[9])]+arry[100]
    if x[-2:] == '00':
        return text_num
    if x[:10] != '0000000000':
        text_num += arry[0.5]
    if x[10] == '1':
        text_num += arry[int(x[10]+x[11])]
        return text_num
    if x[10] != '0' and x[10] != '1':
        text_num += arry[int(x[10]+'0')]
    text_num += arry[int(x[11])]
    return text_num

su = ''
arrx = {
0:'',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',
9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',
15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',
80:'eighty',90:'ninety',100:'hundred',1000:'thousand',1000000:'million',
1000000000:'billion',0.5:'and'
        }
for i in range(1,1001):
    su += num_to_text(i,arrx)
print('Result of the problem 17:', len(su))
