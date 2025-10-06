while True:
	password = input('Enter Your Password: ')

	requirements = {
				'lowercase': any(c.islower() for c in password),
		 		'uppercase': any(c.isupper() for c in password),
		 		'digit': any(c.isdigit() for c in password),
		 		'length': len(password) >= 8
		 		}

	failed_requirements = [key for key, passed in requirements.items() if not passed]

	if not failed_requirements:
		print('password created')
		break
	else:
		print('password missing requirements: ')
		for i in failed_requirements:
			print(f'{i}')