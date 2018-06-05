# -*- coding: utf-8 -*-
"""
Created on Tue May 22 22:59:18 2018

@author: gator
"""



def minMonthlyPayment(balance, interestRate, payment):
    '''
   Returns the remianing balnce after one year
    '''
    for i in range (12):
        balance = balance - payment
        balance = balance + (interestRate * balance)
    return balance


totalBalance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0
x = 1
monthlyPayment = 0
while x > 0:
    x = minMonthlyPayment(totalBalance, monthlyInterestRate, monthlyPayment)
    monthlyPayment += 10
print("Lowest Payment: " + str(monthlyPayment - 10))