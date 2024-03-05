#!/usr/bin/env python3
"""
fileName: temp_conveter.py
author: Hezha
dateAndTime: 3/4/24-23:10
description: conver C to F
"""
from calculate import add, sub, mult, div

def cToF(c):
    return add(mult(c,1.8),32)

def fToC(f):
    return mult(sub(f,32),div(5,9))

def menu():
    print("\n***\tMENU\t***")
    print("1- Fahrenheit To Celsius")
    print("2- Celsius to Fahrenheit")
    print("3- Exit")

def main():
    while 1==1:
        menu()
        op = input("Select an option: ")
        if op=="1":
            f = input("Enter Fahrenheit tempeture: ")
            print(f"\nThe tempeture in Ceelsius is {fToC(f)}")
        elif op=="2":
            c = input("Enter Celsius tempeture: ")
            print(f"\.The tempeture in Fahrenheit is {cToF(c)}")
        elif op=="3":
            break
        else:
            print("Invalid input!")

if __name__=="__main__":
    main()