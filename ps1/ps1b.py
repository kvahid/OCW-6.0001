# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:50:04 2019

@author: Vahid Karimi

MIT OCW Course 6.0001

Problem SET 1
    
Part B: Saving, with a raise
"""

#assumptions:
portion_down_payment = 0.25
current_saving = 0.0
r = 0.04 #annual rate of return on investment

#user inputs:
annual_salary = float(input("Enter your annual salary in USD: "))
portion_saved = 0.01*float(input("Enter the percent of salary which you wish to save: "))
total_cost = float(input("How much is cost of your dream house in USD? "))
semi_annual_raise = 0.01*float(input("Enter the semi_annual raise as percent: "))

#initialize the month_counter
month_counter = 0

#main loop
while current_saving < portion_down_payment*total_cost:
    #salary raise every six months
    if ((month_counter % 6) == 0) and (month_counter > 0):
        annual_salary *= 1 + semi_annual_raise
    current_saving += current_saving*r/12 + portion_saved*annual_salary/12
    month_counter += 1

#output
print("\nNumber of months:", month_counter)
