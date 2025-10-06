"""Program calculates average speed.

Author: Enzo Hins
Version: 9/1/2025
"""

total_feet = int(input("Enter a total number of feet: "))

miles = total_feet//5280 
remaining_feet = total_feet % 5280 
furlong = remaining_feet//660
remaining_feet = total_feet % 660
print()

print(f"{total_feet} total feet is {miles} mile(s), " 
	+ f"{furlong} furlong(s), and {remaining_feet} feet.")

