# -*- coding: utf-8 -*-
"""
Created on Mon May 21 19:47:12 2018

@author: gator
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    
    if len(aStr) == 0:
        return False
        
    halfIndex = len(aStr) - 1
    
    if aStr[halfIndex] == char:
        return True
    elif len(aStr) == 1:
        return False
    elif aStr[halfIndex] > char:
        return isIn(char, aStr[:halfIndex])
    elif aStr[halfIndex] < char:
        return isIn(char, aStr[halfIndex:])
    
print(str(isIn("x","abcde")))   