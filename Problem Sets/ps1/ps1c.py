# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:46:13 2021

@author: TARIK
"""

annual_salary = float(input("Your starting salary: "))
total_cost = 1000000
semi_annual_raise = .07
# you should save the down payment in 36 months
months = 36
# down payment is %25
portion_down_payment = 0.25
# annual rate of your investment 
r = 0.04

saving = 0
steps = 0

# to make those decimal, you'll devide to 10000
# min rate %0
min_rate = 0
# max rate %100
max_rate = 10000

# find the middle first for bisection search
guess = (min_rate + max_rate) / 2

# while absolute of saving-down payment greater than 100$
while abs(saving - total_cost*portion_down_payment) >= 100:
    # reset saving to 0 at the beginning of each check
    saving = 0
    # assign annual salary to a new one to avoid unwanted changes on annual salary
    for_annual_salary = annual_salary
    # devide 10000 to make it decimal point
    rate = guess / 10000
    for i in range(36):
        # raise salary every 6 months
        if i%6 == 0 and i>0:
            for_annual_salary += for_annual_salary*semi_annual_raise
        # find the monthly salary
        monthly_salary = for_annual_salary/12
        # total saving -> investment + salary's portion
        saving += monthly_salary*rate + saving*r/12
    # if saving is greater than down payment
    if saving < total_cost*portion_down_payment:
        min_rate = guess
    else:
        max_rate = guess 
    # increment steps 1 to calculate how many steps needed
    steps+=1
    # find the new guess
    guess = (max_rate + min_rate) / 2
    
    if steps > 15:
        break
if steps > 15:
    print("no way to save this amount")
else:
    print("rate: ", rate)
    print("steps: ", steps)
