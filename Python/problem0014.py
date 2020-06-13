# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:38:22 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

#class Solution():
#    def longestCommonPrefix(self, strs):
#        ans = []
#        for _ in range(len(strs)):
#            try:
#                a = [k[0] for k in strs]
#                b = []
#                c = {}
#                for p in a:
#                    if p not in b:
#                        b.append(p)
#                        c[p] = 1
#                    else:
#                        c[p] += 1
#                if len(c.keys()) != 1:
#                    if ans == []:
#                        return ''
#                    else:
#                        return ans
#                else:
#                    ans.append(a[0])
#            except:
#                if ans == []:
#                    return ''
#                else:
#                    return ans
#        else:
#            return ''

#class Solution():
#    def __init__(self):
#        self.prex = []
#    def longestCommonPrefix(self, strs):
#        self.prex = list(strs[0])#.copy()
#        for k in strs[1:]:
#            self.ProcessTwoStrs(self.prex, list(k))
#            if self.prex == []:
#                break
#        print(self.prex)
#        return ''.join(self.prex)
#    def ProcessTwoStrs(self, x, y):
##        a = []
##        print((x))
##        print(len(y))
##        k = 1
##        for k in range(1, min(len(x), len(y)), 1):
##            if x[0:k] != y[0:k]:
##                k -= 1
##                break
#        for i,v in enumerate(x):
##            print(i)
##            print(len(y))
##            print()
#            if i < len(y) and v != y[i]: #and两边前后顺序是有差别的
#                self.prex = y[:i].copy()
#                break
#        self.prex = x.copy()
##        print(k)
##        a.append(x[0:k])
##        self.prex = a.copy()

#class Solution():
#    def longestCommonPrefix(self, strs):
#        if not strs: return ""
#        s1 = min(strs)
#        s2 = max(strs)
#        for i,x in enumerate(s1):
##            print(i)
##            print()
#            if x != s2[i]:
#                return s2[:i] #s1[:i]
#        return s1
    
class Solution():
    def longestCommonPrefix(self, strs):
        if strs == [] or strs == None: #if not strs:
            return ''
        else: #只考虑最大和最小排序了的字符串，它们的公共前缀，就是所有字符串的公共前缀
            s1 = min(strs) #s1是最小排序的字符串，以它为准
            s2 = max(strs)
            for i,x in enumerate(s1):
                if x != s2[i]:
                    return s1[:i]
            return s1

solu = Solution()
strs = ["flower","flow","flight"]
strs = ["fxxx","fxxxx"]
strs = ["fxxxaaaa","fxxxx"]
#strs = ["fxxx","fax","fxxxx"]
#strs = ["flower","flow","flightererer"]
#strs = ["flow","flow","flow"]
#strs = ["dog","racecar","car"]
#solu.longestCommonPrefix(strs)
print(solu.longestCommonPrefix(strs))

time2 = time.perf_counter()
print(time2-time1)











