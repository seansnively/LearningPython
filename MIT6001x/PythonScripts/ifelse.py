# -*- coding: utf-8 -*-
"""
Created on 5/11/2018

@author Sean Snively
"""

x = int(input('Enter an integer '))

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('')
        print('Divisible by 2')
elif x%3 == 0:
    print('')
    print('Divisible by 3')
else:
    print('Not divisible by 2 or 3')
print('Done with conditional')