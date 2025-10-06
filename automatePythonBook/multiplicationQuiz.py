import pyinputplus as pyip
import random
import time

correctAnswers = 0

for i in range(10):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    print(f'{num1} * {num2} = ')
    try:
        user_input = pyip.inputStr(
                                allowRegexes=['^%s$' % (num1*num2)],
                                blockRegexes=[('.*', 'Incorrect!')], 
                                timeout=8, 
                                limit=3
                                )
    except pyip.TimeoutException: 
        print('Out of time!')
    except pyip.RetryLimitException: 
        print('Out of tries!')
    else:
        correctAnswers += 1

time.sleep(1) 
print('Score: %s / %s' % (correctAnswers, 10))