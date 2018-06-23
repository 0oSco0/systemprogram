# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:07:46 2018

@author: Sc
"""

def not_bad(s):
    #print(s.index("not"))
    #print(s.rindex("bad"))
    #if(s.startswith("not")&&s.endswith("bad"))
    notL = s.find("not")
    badR = s.rfind("bad")+3
    if(badR > notL):
        return s.replace(s[notL:badR],"is good")
    else:
        return s
    
print(not_bad('This movie is not so bad'))
print(not_bad('This dinner is not that bad!'))
print(not_bad('This tea is not hot'))
print(not_bad("It's bad yet not"))