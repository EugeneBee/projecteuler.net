#Python 3.7.x
#https://projecteuler.net/problem=61
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
ar3 = set()
ar4 = set()
ar5 = set()
ar6 = set()
ar7 = set()
ar8 = set()
arry = []
for i in range(19,142):
    a3 = int(i*(i+1)/2)
    if 999 < a3 < 10000:
        ar3.add(str(a3))
    a4 = i**2
    if 999 < a4 < 10000:
        ar4.add(str(a4))
    a5 = int(i*(3*i-1)/2)
    if 999 < a5 < 10000:
        ar5.add(str(a5))
    a6 = i*(2*i-1)
    if 999 < a6 < 10000:
        ar6.add(str(a6))
    a7 = int(i*(5*i-3)/2)
    if 999 < a7 < 10000:
        ar7.add(str(a7))
    a8 = i*(3*i-2)
    if 999 < a8 < 10000:
        ar8.add(str(a8))
arry.extend([ar3,ar4,ar5,ar6,ar7,ar8])
for ary in arry:
    arrytemp1 = arry[:]
    arrytemp1.remove(ary)
    for y in ary:
        for arz in arrytemp1:
            for z in arz:
                if y[:2] == z[-2:]:
                    arrytemp2 = arrytemp1[:]
                    arrytemp2.remove(arz)
                    for aru in arrytemp2:
                        for u in aru:
                            if z[:2] == u[-2:]:
                                arrytemp3 = arrytemp2[:]
                                arrytemp3.remove(aru)
                                for aro in arrytemp3:
                                    for o in aro:
                                        if u[:2] == o[-2:]:
                                            arrytemp4 = arrytemp3[:]
                                            arrytemp4.remove(aro)
                                            for ark in arrytemp4:
                                                for k in ark:
                                                    if o[:2] != k[-2:]:
                                                        arrytemp5 = arrytemp4[:]
                                                        arrytemp5.remove(ark)
                                                        for arv in arrytemp5:
                                                            for v in arv:
                                                                if k[:2] == v[-2:]:
                                                                    if v[:2] == y[-2:]:
                                                                        reslt = int(y) + int(v) + int(k) + int(o) + int(u) + int(z)
print('Result of the problem 61:', reslt)
