try:
	value = int(input('Enter a value, please:'))
	print (((value > -15) and (value <= 12)) or ((value > 14) and (value < 17)) or (value >= 19))
except ValueError:
	print('You have inputted not an integer digit or not a digit, the program has been stopped emergency')

