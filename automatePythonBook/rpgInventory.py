inventory = {'rope': 1,'gold': 200, 'torch': 1,
			'dagger': 1,'arrow': 22,'bow': 1}

dragonLoot = ['gold', 'dagger', 'gold', 'gold', 'ruby']

def displayInv(inv):
	amtItems = 0
	print('Inventory: ')
	for k, v in inv.items():
		amtItems += v
		print(k + ': ' + str(v))
	print('You have ' + str(amtItems) + ' Items.')

def addInv(inv, loot):
	for i in range(len(loot)):
		if loot[i] in inv.keys():
			inv[loot[i]] += 1
		else:
			inv.update({loot[i]: 1})

displayInv(inventory)
addInv(inventory, dragonLoot)
displayInv(inventory)