#!/usr/bin/env python
# coding: utf-8

def factorial(num):
    if num == 0:
        return 1
    else:
        return num*factorial(num-1)
n=int(input("Enter a number : "))
print("Factorial of ",n," is =",factorial(n))