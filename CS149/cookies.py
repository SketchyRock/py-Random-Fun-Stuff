"""input cookies and family members, cookies divide evenly, rocky gets remainder.

Author: Enzo Hins
Version: 8/26/2025
"""

cookies = int(input('Enter the number of cookies: '))
family = int(input('Enter the number of family members: '))
cookies_per_family = cookies // family
cookies_for_rocky = cookies % family
print()
print(f'Each family member gets {cookies_per_family} cookies, '
	+ f'and Rocky gets {cookies_for_rocky} cookies.')