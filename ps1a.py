# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:21:41 2019

@author: Vahid Karimi

MIT OCW Course 6.0001

Problem SET 1

Problem Description:
    
Part A: House Hunting

You have graduated from MIT and now have a great job!
You move to the San Francisco Bay Area anddecide that you want to start saving 
to buy a house.
As housing prices are very high in the Bay Area, you realize you are going to 
have to save for several years before you can afford to make the downpayment on 
a house. 
In Part A, we are going to determine how long it will take you to save 
enough money to make the down payment given the following assumptions:
    1.Call the cost of your dream home ​total_cost​.
    2.Call the portion of the cost needed for a down payment 
    ​portion_down_payment​. For simplicity, assume that 
    portion_down_payment = 0.25 (25%).
    3.Call the amount that you have saved thus far ​current_savings​. You start 
    with a current savings of $0. 
    4.Assume that you invest your current savings wisely, with an annual 
    return of ​r ​(in other words, at the end of each month, you receive an 
    additional ​current_savings*r/12​ funds to put intoyour savings – the 12 is 
    because ​r​ is an annual rate). Assume that your investments earn a return 
    of r = 0.04 (4%).
    5.Assume your annual salary is ​annual_salary​.
    6.Assume you are going to dedicate a certain amount of your salary each 
    month to saving for the down payment. Call that ​portion_saved​. This 
    variable should be in decimal form (i.e. 0.1 for 10%). 
    7.At the end of each month, your savings will be increased by the return 
    on your investment, plus a percentage of your ​monthly salary 
    ​(annual salary / 12).
    
Write a program to calculate how many months it will take you to save up enough 
money for a downpayment. You will want your main variables to be floats, so you 
should cast user inputs to floats.1
Your program should ask the user to enter the following variables:
    1.The starting annual salary (annual_salary)
    2.The portion of salary to be saved (portion_saved)
    3.The cost of your dream home (total_cost)
    
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