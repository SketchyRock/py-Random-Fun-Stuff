"""Takes first middle and last name and creates a monogram with them.

Author: Enzo Hins
Version: 26/8/2025
"""

first = input('First name? ')
middle = input('Middle name? ')
last = input('Last name? ')
print()
print(f'The customer {first} {middle} {last} has ordered a sweater with the monogram ' 
	+ f'{first[0] + middle[0] + last[0]}.')