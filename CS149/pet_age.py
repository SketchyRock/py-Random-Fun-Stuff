"""Program calculates human age from dog/cat age.

Author: Enzo Hins
Version: 9/3/2025
"""

animal = input("Type: ")
age = int(input("Age: "))
human_age = 0

if animal not in ("dog", "cat"):
    print("Pet type not recognized.")
else:
    if animal == "dog":
        if age < 3:
            human_age = age * 12
        else:
            human_age = 24 + ((age - 2) * 4)
    else:
        if age < 3 and age != 1:
            human_age = age * 12
        elif age == 1:
            human_age = 15
        else:
            human_age = 24 + ((age - 2) * 4)

    print(f"Your {animal}'s age in human years is {human_age}.")