#-*- coding: utf-8 -*-
"""
Created on Sat Jun 23 15:09:02 2018

@author: Sc
"""

#1: 開始
#f1 = open('test.txt', 'r')
#f1 = open('/etc/passwd')
#f1 = open('/etc/passwd', 'rU')
#f2 = open('test.out', 'w')
#3: 終了
#f1.close()
#2: 読み書き
#str = f1.read()
#str = f1.readline()
#list = f1.readlines()
#f2.write(str)
#f2.writelines(list)

#f = open('/etc/passwd', 'rU')
#all = f.read()
#f.close()

f = open('test.txt', 'rU')
for line in f:
    print(line, end='')
f.close()