# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 19:23:08 2019

@author: Vahid Karimi

Problem SET 1
    
Part C: Finding the right amount to save away
"""

#assumptions
semi_annual_raise = 0.07
r = 0.04
portion_down_payment = 0.25
total_cost = 1000000.0
epsilon = 100.0

#initialization
lower_guess = 0
upper_guess = 10000
current_saving = 0.0
step = 0
starting_salary = float(input("Enter the starting salary: "))
annual_salary = starting_salary

#check the possibility
guess = upper_guess
for i in range(36):
    if ((i % 6) == 0) and (i > 0):
        annual_salary *= 1 + semi_annual_raise
    current_saving += current_saving*r/12 + 0.0001*guess*annual_salary/12
    
if current_saving < portion_down_payment*total_cost - epsilon:
    print("It is not possible to pay the down payment in three years")
else:
    #first guess
    guess = (lower_guess + upper_guess) / 2
    for i in range(36):
        if ((i % 6) == 0) and (i > 0):
            annual_salary *= 1 + semi_annual_raise
        current_saving += current_saving*r/12 + 0.0001*guess*annual_salary/12
        
        #main loop for possible scenarios       
    while abs(current_saving - portion_down_payment*total_cost) > epsilon:
        step += 1
        if current_saving > portion_down_payment*total_cost:
            upper_guess = (upper_guess + lower_guess) / 2
        else:
            lower_guess = (upper_guess + lower_guess) / 2
        current_saving = 0.0
        annual_salary = starting_salary
        guess = (lower_guess + upper_guess) / 2
        for i in range(36):
            if ((i % 6) == 0) and (i > 0):
                annual_salary *= 1 + semi_annual_raise
            current_saving += current_saving*r/12 + 0.0001*guess*annual_salary/12
                
    print("Best saving rate:", "{0:0.4f}".format(guess/10000))
    print("Steps in bisection search:", step)
                
