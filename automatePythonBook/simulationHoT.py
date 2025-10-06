import random
import time

hCount = 0
tCount = 0

def coinFlipGen():
	coinFlipList = []

	for i in range(100):
		if (random.randint(0,1) == 0):
			coinFlipList.append('H')
		else:
			coinFlipList.append('T')

	for i in coinFlipList:
		print(i, end='', flush=True)
		time.sleep(0.0001)
	print()

	return coinFlipList

def sixStreakCount(randList):
	headStreak = 0
	tailStreak = 0
	global hCount
	global tCount

	for i in randList:
		if i == 'H':
			headStreak += 1
			tailStreak = 0
			if headStreak == 6:
				hCount += 1
				headStreak = 0
		if i == 'T':
			tailStreak += 1
			headStreak = 0
			if tailStreak == 6:
				tCount += 1
				tailStreak = 0

def hundredIterations():
	for i in range(100):
		sixStreakCount(coinFlipGen())

	print()
	print(hCount, tCount)

#Main func
hundredIterations()


