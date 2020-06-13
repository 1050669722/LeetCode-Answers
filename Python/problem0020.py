# -*- coding: utf-8 -*-
"""
Created on Mon May 13 16:32:41 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution(): #16:34 - 16:58
#    def isValid(self, s):
#        d = {'key1':0,
#             'key2':0,
#             'key3':0}
#        for k in s:
#            if k == '(':
#                if d['key2'] >= 0 and d['key3'] >= 0:
#                    d['key1'] += 1
#                else:
#                    return False
#            if k == ')':
#                if d['key2'] <= 0 and d['key3'] <= 0:
#                    d['key1'] -= 1
#                else:
#                    return False
#            if k == '[':
#                if d['key1'] >= 0 and d['key3'] >= 0:
#                    d['key2'] += 1
#                else:
#                    return False
#            if k == ']':
#                if d['key1'] <= 0 and d['key3'] <= 0:
#                    d['key2'] -= 1
#                else:
#                    return False
#            if k == '{':
#                if d['key1'] >= 0 and d['key2'] >= 0:
#                    d['key3'] += 1
#                else:
#                    return False
#            if k == '}':
#                if d['key1'] <= 0 and d['key3'] <= 0:
#                    d['key3'] -= 1
#                else:
#                    return False
#            
#        if d['key1']==0 and d['key2']==0 and d['key3']==0:
#            return True
#        else:
#            return False

#class Solution():
#    def isValid(self, s):
#        while '{}' in s or '()' in s or '[]' in s: #问题的本质是s里面一定要有有效的括号
#            s = s.replace('{}', '')
#            s = s.replace('[]', '')
#            s = s.replace('()', '')
#        return s == ''

#class Solution():
#    def isValid(self, s):
#        while ('()' in s) or ('[]' in s) or ('{}' in s):
#            s = s.replace('()','')
#            s = s.replace('[]','')
#            s = s.replace('{}','')
#        return s == ''

#class Solution():
#    def isValid(self, s):
#        a = []
#        for k in range(len(s)):
#            if a == []:
#                a.append(s[k])
#            else:
#                a.append(s[k])
#                if (a[-1] == ')' and a[-2] == '(') or (a[-1] == ']' and a[-2] == '[') or (a[-1] == '}' and a[-2] == '{'):
#                    a.pop()
#                    a.pop()
#        return not a

#class Solution():
#    def isValid(self, s):
#        a = []
#        for k in range(len(s)):
#            a.append(s[k])
#            if len(a) >= 2:
#                if (a[-1] == ')' and a[-2] == '(') or (a[-1] == ']' and a[-2] == '[') or (a[-1] == '}' and a[-2] == '{'):
#                    a.pop()
#                    a.pop()
#        return not a

#class Solution():
#    def isValid(self, s):
#        a = []
#        for k in range(len(s)):
#            if a == []:
#                a.append(s[k])
#            elif (s[k] == ')' and a[-1] == '(') or (s[k] == ']' and a[-1] == '[') or (s[k] == '}' and a[-1] == '{'):
#                a.pop()
#            else:
#                a.append(s[k])
#        return not a

class Solution():
    def isValid(self, s):
        left_1, left_2, left_3 = 0, 0, 0
        for k in s:
            if k == '(':
                left_1 += 1
            if k == ')':
                left_1 -= 1
            if k == '[':
                left_2 += 1
            if k == ']':
                left_2 -= 1
            if k == '{':
                left_3 += 1
            if k == '}':
                left_3 -= 1
        return (not left_1) and (not left_2) and (not left_3)

solu = Solution()
s = '()'
s = "()[]{}"
s = "(]"
s = "([)]"
s = "{[]}"
s = "([)]"
print(solu.isValid(s))
            
time2 = time.perf_counter()
print(time2-time1)







