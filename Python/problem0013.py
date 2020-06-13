# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:01:52 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class Solution(): #10:10 - 
    def __init__(self):
#        self.ans = 0
#        self.val = 0
        self.special = ('IV','IX','XL','XC','CD','CM')
    def romanToInt(self, s):
        a = list(s)
        b = []
#        self.ans = []
#        special = ('IV','IX','XL','XC','CD','CM')
        while a != []: #a != None, bool(a), a
            try:
                c = a
                b.append(a.pop(0))
                b.append(a.pop(0))
                if ''.join(b) in self.special:
#                    print(1)
                    self.convert(b)
                else:
#                    print(2)
#                    print(a)
                    b = c.pop(0)
#                    print(b)
                    self.convert(b)
            except:
#                print(3)
                b.append(a.pop(0))
                self.convert(b)
        return self.ans
    def convert(self, x):
#        print(x)
#        special = ('IV','IX','XL','XC','CD','CM')
#        if ''.join(x) in self.special:
        try:
#            print(''.join(x))
            self.SingleLetterToNumber(list(x)[1])
            self.SingleLetterToNumber(list(x)[0])
            self.ans = self.val[0]- self.val[1]                    
#        else:
        except:
#            print(x)
            self.SingleLetterToNumber(x)
    def SingleLetterToNumber(self, x):
        d = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000}
#        self.val = d[x]
        self.val.append(d[x])
            
solu = Solution()
s = "III"
#s = "IV"
#s = "IX"
#s = "LVIII"
#s = "MCMXCIV"
print(solu.romanToInt(s))
#print(solu.romanToInt(s))
#print(type(solu.romanToInt(s)))

time2 = time.perf_counter()
print(time2-time1)
