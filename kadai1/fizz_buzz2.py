# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 09:00:25 2018

@author: Sc

"""
def fb(i):
    x = i%15
    y = {0:"FizzBuzz",3:"Fizz",5:"Buzz",6:"Fizz",9:"Fizz",10:"Buzz",12:"Fizz"}
    #y = ["FizzBuzz","","","Fizz","","Buzz","Fizz","","","Fizz","Buzz","","Fizz","",""]
    return y.get(x)
    
    
i = 1
while i <= 200:
    print(i, fb(i))
    i = i + 1