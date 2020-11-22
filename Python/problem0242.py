# -*- coding: utf-8 -*-
"""
Created on Tue May 28 17:42:36 2019

@author: Administrator
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#        return len(s) == len(t) and set(s) == set(t)
        a = {}
        b = {}
        for k in s:
            try:
                a[k] += 1
            except:
                a[k] = 1
        for k in t:
            try:
                b[k] += 1
            except:
                b[k] = 1
        return a == b
    
    
# from collections import Counter

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return Counter(s) == Counter(t)
    
    
solu = Solution()
s, t = "anagram", "nagaram"
#s, t = "rat", "car"
s, t = 'aa', 'a'
s, t = "aacc", "ccac"
print(solu.isAnagram(s, t))
