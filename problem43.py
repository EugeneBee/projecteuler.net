#Python 3.7.x
#https://projecteuler.net/problem=43
"""
There is a deliberate error in the code. 
Do you understand Python for a long time to find her.
"""
import itertools
summ = 0
for i in list(itertools.permutations(set([1,2,3,4,5,6,7,8,9,0]))):
	var = ''
	for z in i:
		var += str(z)
	if int(var[1:4]) % 2 == 0:
		if int(var[2:5]) % 3 == 0:
			if int(var[3:6]) % 5 == 0:
				if int(var[4:7]) % 7 == 0:
					if int(var[5:8]) % 11 == 0:
						if int(var[6:9]) % 13 == 0:
							if int(var[7:]) % 16 == 0:
								summ += int(var)
print('Result of the problem 43:', summ)
