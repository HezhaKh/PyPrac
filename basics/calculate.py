#!/usr/bin/env python3
"""
fileName: calculate.py
author: Hezha
dateAndTime: 3/2/24-21:28
description: ask for 2 numbers then execute the selected operation user wants
"""

def add(no1,no2):                       # Addition operation
    return float(no1)+float(no2)

def sub(no1,no2):                       # Subtraction operation
    return float(no1)-float(no2)

def mult(no1,no2):                      # Multiplication operation
    return float(no1)*float(no2)

def div(no1,no2):                       # Division operation
    return float(no1)/float(no2)

def menu():                             # Main Menu printout
    print("\n***\tMenu\t***")
    print("1-Addition")
    print("2-Subtraction")
    print("3-Multiplication")
    print("4-Division")
    print("5-Exit")

def main():

    no1 = input("Enter the first number: ")     # Ask for user input
    no2 = input("Enter the second number: ")
    
    while 1==1:
        menu()                                      # Print menu
        op = input("Select desired operation: ")    # Ask for operation
        if op == "1":
            print(add(no1,no2))
        elif op == "2":
            print(sub(no1,no2))
        elif op == "3":
            print(mult(no1,no2))
        elif op == "4":
            print(div(no1,no2))
        elif op == "5":
            break
        else:
            print("Invalid input.")

if __name__=="__main__":
    main()