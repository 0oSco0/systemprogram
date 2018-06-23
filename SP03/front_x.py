# -*- coding: utf-8 -*-
"""
Created on Tue Jun 19 17:25:33 2018

@author: Sc
"""

def front_x(x):
    count = 0
    x.sort()
    #for str in x:
    for str in reversed(x):
    #while x.pop():
        if(str[0:1] == 'x'):
            count = count + 1
    #return x[-count:]+x[0:len(x)-count]
    return x[-count:]+x[0:-count]
       
print(front_x(['bbb','ccc','axx','xzz','xaa']))
print(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']))
print(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']))
