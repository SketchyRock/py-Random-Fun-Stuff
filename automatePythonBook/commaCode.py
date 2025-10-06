import sys

userList = []

def getUserList10(randomList):
	for i in range(0,10):
		randomList.append(input('Enter list item ' + str(i) + ':'))
		if (randomList[i] == 'exit'):
			randomList.remove('exit')
			break	


def commaCode(randomList):
	decision = input("Want me to do something wacky? Y/N: ")
	if decision == ('Y' or 'y'):
		for i, item in enumerate(randomList):
			if item == randomList[len(randomList) - 2]:
				print(item + ' and ' + randomList[len(randomList) - 1])
				break
			print(item + ', ', end='')	
	elif (decision == ('N' or 'n')):
		return
	else:
		sys.exit()

#Main exec
getUserList10(userList)
if(userList):
	commaCode(userList)