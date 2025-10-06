"""Program calculates steel grade.

Author: Enzo Hins
Version: 9/3/2025
"""

hardness = int(input("Enter hardness: "))
carbon_content = float(input("Enter carbon content: "))
tensile_strength = int(input("Enter tensile strength: "))

a = hardness > 50
b = carbon_content < 0.7
c = tensile_strength > 5600

if a and b and c:
    grade = 10
elif a and b:
    grade = 9
elif b and c:
    grade = 8
elif a and c:
    grade = 7
elif a or b or c:
    grade = 6
else:
    grade = 5

print(f"Grade: {grade}")