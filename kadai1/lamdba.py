# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:11:33 2018

@author: Sc
"""
a = 2
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

print(sorted(students,key=lambda s: s[2]))
lambda a students:students[2]
#print(key=lambda s: s[2])