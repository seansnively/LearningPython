# -*- coding: utf-8 -*-
"""
Created on Wed May 16 18:16:50 2018

@author: gator
"""


high = 100
low = 0
guess = (high + low) // 2

print("Please think of a number between 1 and 100!")

while True:
    print("Is your secret number? " + str(guess))
    answer = input("Enter 'h' to indicate the guess is too high."
          " Enter 'l' to indicate the guess is too low."
          " Enter 'c' to indicate I guessed correctly: ")
    if answer == "h":
        high = guess
    elif answer == "l":
        low = guess
    elif answer == "c":
        break
    else:
        print("Sorry, I did not understand your input")
    guess = (high + low) // 2
print("Game over. Your secret number was: " + str(guess))  