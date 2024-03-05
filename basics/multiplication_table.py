#!/usr/bin/env python3
"""
fileName: multiplication_table.py
author: Hezha
dateAndTime: 3/5/24-00:29
description: print multiplication table for a number provided
"""
from calculate import mult

def mulTable(no):
    count=0
    while count < 10:
        print(f"{no} X {count} = {mult(no,count)}")
        count=count+1

def main():
    no = input("Please enter a number: ")
    mulTable(no)

if __name__=="__main__":
    main()