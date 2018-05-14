# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:54:21 2018

@author: gator
"""

s = "aaa"

vowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
print("Number of vowels: " + str(vowels))