# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:14:07 2018

@author: Sc
"""

import sys
import re

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rU",encoding='utf-8') 
else:
    f = open("wc.py","rU",encoding='utf-8')
    #f = sys.stdin
    
codelinenum = 1     
for line in f.readlines():
    if (re.match(r'^ *\n',line) or line.startswith('#')):
              print(line,file=sys.stdout, end='')
    #elif(re.match(r"(^ *""")|(^ *''')"):
    else:
        print(codelinenum,line,file=sys.stdout, end='')
        codelinenum = codelinenum + 1
    
f.close()




