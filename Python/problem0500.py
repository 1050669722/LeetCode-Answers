# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:55:53 2019

@author: Administrator
"""

class Solution:
    def findWords(self, words: list) -> list:
        d = {'q':1,'w':1,'e':1,'r':1,'t':1,'y':1,'u':1,'i':1,'o':1,'p':1,
             'a':2,'s':2,'d':2,'f':2,'g':2,'h':2,'j':2,'k':2,'l':2,
             'z':3,'x':3,'c':3,'v':3,'b':3,'n':3,'m':3,}
        a = []
        for p in words:
            if len(p)<=1:
                a.append(p)
            mark = 1#d[p[0].lower()]
#            print(Sum)
            for q in range(1, len(p)):
                if d[p[q].lower()] != d[p[q-1].lower()]:
                    mark = 0
#                Sum -= d[p[q].lower()]
#                print(Sum)
                if mark == 0: #Sum != 0:
                    break
                if q == len(p)-1:
                    a.append(p)
        return a
        
solu = Solution()
words = ["Hello", "Alaska", "Dad", "Peace"]
#words = ["Alaska"]
print(solu.findWords(words))