"""Takes price, amount, and grocerie, returns the average price per item.

Author: Enzo Hins
Version: 26/8/2025
"""

name = input('Enter the item name: ')
num = input('Enter the number purchased: ')
price = input('Enter the total price: ')
avg_price = float(price) / int(num)
print()
print(f'The average price of a(n) {name} is {avg_price:.2f} dollars.')