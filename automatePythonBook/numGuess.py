import sys
import random

randNum = random.randint(1,100)

print('Guess my number between 1 & 100')

guess = int(input())

while (guess != randNum):
	if (guess > randNum):
		print('lower, guess again')
		try:
			guess = int(input())
		except ValueError:
			print('enter correct value')
	else:
		print ('higher, guess again')
		try:
			guess = int(input())
		except ValueError:
			print('enter correct value')		

print('yay, you got it')
sys.exit()
