# -*- coding: utf-8 -*-
"""
Created on 5/11/2018

@author Sean Snively
"""

#Bisection search

x = float(input("Enter a number greater than one: "))
epsilon = .01
high = x
low = 1.0
count = 0
guess = (high + low) / 2

while abs(guess**2 - x) >= epsilon:
    print("low: " + str(low) + " high: " + str(high) + " guess: " + str(guess))
    count+=1
    if guess**2 < x:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2
print("Number of guesses: " + str(count))
print(str(guess) + " is close to the square root of " + str(x))        