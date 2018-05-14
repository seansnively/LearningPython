# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:54:21 2018

@author: gator
"""

s = "bobaaabobaaabob"

bob = 0
index = 0
while index < len(s) - 2:
    if s[index:index + 3] == 'bob':
        bob += 1
    index += 1
print("Number of times bob occurs is: " + str(bob))