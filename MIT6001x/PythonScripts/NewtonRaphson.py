# -*- coding: utf-8 -*-
"""
Created on Wed May 16 21:43:54 2018

@author: gator
"""

epsilon = .01
y = 54.0
guess = y / 2.0
numGuesses = 0

while abs(guess*guess - y) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - y) / 2 * guess)
print("number of guesses = " + str(numGuesses))
print("Square root of " + str(y) + " is about " + str(y))