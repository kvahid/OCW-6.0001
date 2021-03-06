# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:21:41 2019

@author: Vahid Karimi

MIT OCW Course 6.0001

Problem SET 1
    
Part A: House Hunting
    
"""

#assumptions:
portion_down_payment = 0.25
current_saving = 0.0
r = 0.04 #annual rate of return on investment

#user inputs:
annual_salary = float(input("Enter your annual salary in USD: "))
portion_saved = 0.01*float(input("Enter the percent of salary which you wish to save: "))
total_cost = float(input("How much is cost of your dream house in USD? "))

#initialize the month_counter
month_counter = 0

#main loop
while current_saving < portion_down_payment*total_cost:
    current_saving += current_saving*r/12 + portion_saved*annual_salary/12
    month_counter += 1

#output
print("\nNumber of months:", month_counter)