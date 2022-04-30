# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 18:00:28 2021

@author: TARIK
"""

annual_salary = float(input("Your annual salary: "))
portion_saved = float(input("How many % of your salary you want to save each month? "))/100
total_cost = float(input("Total cost of your dream home? "))

# you have 0$ at the beginning
current_savings = 0
# down payment is %25
portion_down_payment = total_cost * 0.25
# annual rate of your investment 
r = 0.04
# set a counter for months
months = 0

# while current savings < down payment
while current_savings < portion_down_payment:
    # savings will increase at the end of every month from investment and portion of salary
    current_savings += current_savings*r/12 + portion_saved*annual_salary/12
    # increment months at the end of each month
    months+=1

print("Number of months", months)
