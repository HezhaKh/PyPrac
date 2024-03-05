#!/usr/bin/env python3
"""
fileName: age_calculator.py
author: Hezha
dateAndTime: 3/4/24-22:16
description: Ask for user age and calculate
"""
from calculate import sub

year = input("What year is this? ")
birthDay = input("When did you pop out of yo mama's minge? ")

if sub(year, birthDay) >= 100:
    print("You dead!")
elif 70 <= sub(year, birthDay) < 100:
    print("You mummy!")
elif 40 <= sub(year, birthDay) <70:
    print("Time for elder care you old fuck!")
elif 30 <= sub(year, birthDay) < 40:
    print("Kids call you old!")
elif 20 <= sub(year, birthDay) < 30:
    print("You feel old but you aint!")
else:
    print("You kid!")