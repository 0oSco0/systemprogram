# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 19:01:10 2018

@author: Sc
"""
li = ["gutenberg", "a", "all", "alice", "project"]
def foo(s):
    return s[-1]

print(sorted(li, key=foo))
print(sorted([[1, 7], [1, 3], [3, 4, 5], [2, 2]],key=foo))