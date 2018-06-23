# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 18:28:52 2018

@author: Sc
"""

def sort_last(x):
    Xx = []
    for str in x:
        Xx.append(str[-1:]+str[0:-1])
    #print(Xx)
    Xx.sort()
    #print(Xx)
    x = []
    for str in Xx:
        x.append(str[1:]+str[0:1])
    return x
print(sort_last([[1, 3], [3, 2], [2, 1]]))
print(sort_last([[2, 3], [1, 2], [3, 1]]))
print(sort_last([[1, 7], [1, 3], [3, 4, 5], [2, 2]]))