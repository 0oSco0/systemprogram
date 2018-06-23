# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:53:13 2018

@author: Sc
"""
import time, random
sum=0
before = time.clock()
for i in range(1000000):
    sum = sum + random.randint(1,100)
gaptime = time.clock() - before
print ( "gaptime:" , gaptime , flush = True)