# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 16:51:42 2018

@author: Sc
"""

def match_ends(li):
    count=0
    for str in li:
        if(len(str)>=2 and str[0:1]==str[-1:]):
            count=count+1
    return count
                
            
print(match_ends(['aba','xyz','aa','x','bbb']))
print(match_ends(['','x','xy','xyx','xx']))
print(match_ends(['aaa','be','abc','hello']))