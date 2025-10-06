"""Checks payroll whatever.

Author: Enzo Hins
Version: 25/8/2025
"""
print("What is your name?", end=' ')
Name = input()
print("How many hours did you work this week?", end=' ')
h = int(input())
print("What is your hourly pay rate?", end=' ')
payrate = float(input())
grosspay = int(h)*float(payrate)
bonus = 500
grosspay = grosspay+bonus
print("Hello " + Name)
print("Your gross pay is $", grosspay)