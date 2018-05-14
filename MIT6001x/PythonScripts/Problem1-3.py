# -*- coding: utf-8 -*-
"""
Created on Sun May 13 22:54:21 2018

@author: gator
"""

s = "abcdbzzzzzz"

newordo = 0
ordohold = 0
news = ""
finals = ""

for char in s:
    newordo = ord(char)
    if newordo >= ordohold:
        news += char
        ordohold = newordo
    else:
        ordohold = newordo
        news = char
    if len(news) > len(finals):
        finals = news
print ("Longest substring in alphabetical order is: " + finals)
        
        
        