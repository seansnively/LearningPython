# -*- coding: utf-8 -*-
"""
Created on Mon May 21 23:31:36 2018

@author: gator
"""
#fnds the balance remaing after 12 minimum payments
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12.0
for i in range (12):
    minMonthlyPayment = monthlyPaymentRate * balance
    balance = balance - minMonthlyPayment
    balance = balance + (monthlyInterestRate * balance)
print(str(round(balance, 2)))    