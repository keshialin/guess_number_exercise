import random

while True:
	start = int(input('Please enter a start number:'))
	end = int(input('Please enter an end number:'))
	if start < end:
		r = random.randint(start, end)
		break
	else:
		print('start number should not be larger than end number!')


count = 0
while True:
	count += 1
	num = input('Please guess a number from {} to {}:'.format(start, end))
	num = int(num)
	if num == r:
		print('You are right!')
		print('You\'ve guessed for {} times!'.format(count))
		break
	elif num > r:
		print('Your answer is larger than the answer!')
	elif num < r:
		print('Your answer is smaller than the answer!')
	print('You\'ve guessed for {} times!'.format(count))
