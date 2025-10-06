"""Program calculates average speed.

Author: Enzo Hins
Version: 9/1/2025
"""

miles = float(input("How many miles did you race? "))
print("How much time did that take you in hours, minutes, and seconds?")
hours = float(input("  Hours: "))
minutes = float(input("  Minutes: "))
seconds = float(input("  Seconds: "))
print()

time_hours = (hours + (minutes / 60) + (seconds / 3600))
avg_speed_mph = miles / time_hours
avg_speed_kmh = (miles*1.60934) / time_hours

print(f"Your speed was {avg_speed_mph:.2f} mph, which is {avg_speed_kmh:.2f} kph.")