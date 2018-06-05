# -*- coding: utf-8 -*-
"""
Created on Tue May 22 23:10:09 2018

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

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0

monthlyPayLow = balance / 12
monthlyPayHigh = (balance*(1 + monthlyInterestRate)**12) / 12

count = 0
while True:
    monthlyPayment = (monthlyPayHigh + monthlyPayLow) / 2
    x = minMonthlyPayment(balance, monthlyInterestRate, monthlyPayment)
    if abs(x) < .01:
        break
    elif x > .01:
        monthlyPayLow = monthlyPayment
    elif x < -.01:
        monthlyPayHigh = monthlyPayment
print("Lowest Payment: " + str(round(monthlyPayment, 2)))