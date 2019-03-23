# -*- coding: utf-8 -*-
"""
MIT OCW Course 6.0001

Problem SET 0

Developer: Vahid Karimi

Problem Description:
    
   Write a program that does the following in order: 
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y”  
3. Prints out number “x”, raised to the power “y”. 
4. Prints out the log (base 2) of “x”.  
"""
#importing log function from math library
from math import log

#asking the user to enter two numbers for x and y and changing the numbers to float type
x = float(input("Enter a number: "))
y = float(input("Enter another number: "))

#creating the output strings
s1 = str(x) + ' raised to the power of ' + str(y) + ' = ' + str(x**y)
s2 = 'log (base 2) of ' + str(x) + ' = ' + str(log(x, 2))

#printing out the outputs
print('\n')
print(s1)
print(s2)