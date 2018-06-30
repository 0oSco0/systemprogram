# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 10:14:07 2018

@author: Sc
"""

import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
    #f = open("test.txt","rU",encoding='utf-8')
elif argc == 2:
    try:
        f = open(sys.argv[1],"rU")
    except IOError:
        sys.exit("wc: %s: No such file or directory" % (sys.argv[1]))
else:
    sys.exit("usage: wc [file]")
    
"""
文字	意味
'r'	読み込み用に開く (デフォルト)
'w'	書き込み用に開き、まずファイルを切り詰める
'x'	排他的な生成に開き、ファイルが存在する場合は失敗する
'a'	書き込み用に開き、ファイルが存在する場合は末尾に追記する
'b'	バイナリモード
't'	テキストモード (デフォルト)
'+'	ディスクファイルを更新用に開く (読み込み／書き込み)
'U'	ユニバーサル改行 モード (非推奨)
"""
    
d = {}    
for s in f:
    #print(s,file=sys.stdout, end='')
    s = s.lower()
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('-', '')
    s = s.replace('_', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    s = s.replace('"', '')
    s = s.replace("'", '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('/', '')
    words = s.split()
    #print(words)
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    #print(d)
    
f.close()
print("Number of words:", len(words))

def foo(s):
    return d[s]

sorted_keys = sorted(d.keys(), key=foo, reverse=True)#降順

#sorted_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
#print("Number of words:", len(words))
print("Top 20 frequent words:")
i = 0
for k in sorted_keys:
    if i == 20:
        break
    print(" {}: {}".format(k, d[k]))
    i += 1
    

