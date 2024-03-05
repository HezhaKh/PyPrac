#!/usr/bin/env python3
"""
fileName: interest_calculator.py
author: Hezha
dateAndTime: 3/5/24-00:01
description: calculates the simple interest for a given principal.
"""
from calculate import mult,div

def interest(p,r,t):
    return mult(mult(p,div(r,100)),div(t,12))

def main():
    while True:
        p=input("What is the principal amount? ")
        r=input("What is the rate if intrest per year? ")
        t=input("How many months? ")
        print(f"The amout of interest is {interest(p,r,t)}\n")

if __name__=="__main__":
    main()