import re

date = ''
print('xx/xx/xxxx')

date_regex = re.compile(r'(\d{2})/(\d{2})/(\d{4})')
date_input = '/'.join([input(i) for i in ('Day: ', 'Month: ', 'Year: ')])

mo = date_regex.search(date_input)
day, month, year = (int(mo.group(i)) for i in range(1,4))

days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30,
    5: 31, 6: 30, 7: 31, 8: 31,
    9: 30, 10: 31, 11: 30, 12: 31
}

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
	days_in_month[2] = 29

if month in days_in_month and 1 <= day <= days_in_month[month]:
	print('valid date')
else:
	print('invalid date')