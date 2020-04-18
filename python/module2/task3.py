import random

def getting_number():
	value = input('Input a positive number: ')

	while not value.isdigit():
		value = input('You have inputted not a number or neggative number, try one more time: ')

	return value

random_value = random.randint(1,100)
print('I made up a random value from 1 to 100, could you guess it?')

value = int(getting_number())

while (value != random_value):
	if (value > random_value):
		print('Too high, try one more time: ')
		value = int(getting_number())
	else:
		print('Too low, try one more time: ')
		value = int(getting_number())
else:
	print(f'You are right, the made value is {random_value}')
