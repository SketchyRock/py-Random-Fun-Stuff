tableData = [['apples', 'oranges', 'cherries', 'banana'],
			['Alice', 'Bob', 'Carol', 'David'],
			['dogs', 'cats', 'moose', 'goose']]

def printTable(data):
	maxColWidth = [max(len(item) for item in col) for col in data]

	for row in range(len(data[0])):
		for col in range(len(data)):
			print(data[col][row].rjust(maxColWidth[col]), end=' ')
		print()

	
printTable(tableData)