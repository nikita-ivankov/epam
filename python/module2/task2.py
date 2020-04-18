from sys import argv
from math import sqrt

try:
	if (len(argv) != 4):
		print('The amount of arguments you have inputted is not enough or too high')
	elif ((int(argv[1]) <= 0) or (int(argv[2]) <= 0) or (int(argv[3]) <= 0)):
		print('The length can not be negative or equal zero')
	else:
		parties = [int(x) for x in argv[1:]]
		p = (parties[0] + parties[1] + parties[2])/2
		print(f'The result is {sqrt(p*(p-parties[0])*(p-parties[1])*(p-parties[2]))}')
except ValueError:
	print('You have given wrong value, the program has been stopped emergency')
