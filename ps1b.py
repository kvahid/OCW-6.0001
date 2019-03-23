# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:50:04 2019

@author: Vahid Karimi

MIT OCW Course 6.0001

Problem SET 1

Problem Description:
    
Part B: Saving, with a raise
Background
    In Part A, we unrealistically assumed that your salary didn’t change.  But you 
    are an MIT graduate, and clearly you are going to be worth more to your company 
    over time! So we are going to build on your solution to Part A by factoring in a 
    raise every six months. In ​ps1b.py​, copy your solution to Part A (as we are 
    going to reuse much of that machinery).  Modify your program to include the 
    following:
        
1. Have the user input a semi-annual salary raise ​semi_annual_raise​ 
    (as a decimal percentage)
2. After the 6​th​ month, increase your salary by that percentage. Do the same 
    after the 12th​ month, the 18th​​ month, and so on. Write a program to 
    calculate how many months it will take you save up enough money for a 
    downpayment.  Like before, assume that your investments earn a return of 
    ​r​ = 0.04 (or 4%) and the required down payment percentage is 0.25 (or 25%).  
    Have the user enter the following variables:
        1.The starting annual salary (annual_salary)
        2.The percentage of salary to be saved (portion_saved)
        3.The cost of your dream home (total_cost)
        4.The semi­annual salary raise (semi_annual_raise)
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
    #salary raise logic
    if ((month_counter % 6) == 0) and (month_counter > 0):
        annual_salary *= 1 + semi_annual_raise
    current_saving += current_saving*r/12 + portion_saved*annual_salary/12
    month_counter += 1

#output
print("\nNumber of months:", month_counter)