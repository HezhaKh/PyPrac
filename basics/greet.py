#!/usr/bin/env python3
"""
fileName: greet.py
author: Hezha
dateAndTime: 3/2/24-21:09
decription: Ask user for name and print greeting.
"""


name=input("Enter your name: ")

print("Hello, " + name + "! Welcome to Python scripting.")

print(f"Hello, {name}! Welcome to Python scripting.")

print("Hello, {}! Welcome to Python scripting.".format(name))