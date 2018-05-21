# -*- coding: utf-8 -*-
"""
Created on Mon May 21 18:52:05 2018

@author: gator
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    x = min(a, b)
    while x > 1:
        if a % x == 0 and b % x == 0:
            return x
        else:    
            x -= 1
    return 1

print(gcdIter(25,15))

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
    
print(gcdRecur(25,15))    