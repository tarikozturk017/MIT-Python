# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 18:28:01 2021

@author: TARIK
"""

number = float(input("Type a whole number: "))
epsilon = 0.000001
low = 0
high = 100
guess = int((low + high)/2)
steps = 0
while abs(guess - number) != 0:
    if guess < number:
        low = guess
    elif guess > number:
        high = guess
    steps+=1
    guess = int((low + high)/2)
    
print("Steps: ", steps)
print("Guess: ", guess)
    