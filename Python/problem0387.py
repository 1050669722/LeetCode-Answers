# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:31:48 2019

@author: Administrator
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for idx, char in enumerate(s):
            d[char] = idx
        for idx in range(len(s)):
            if idx == d[s[idx]]:
                return idx
            else:
                d[s[idx]] = -100#pass#
        return -1
        
        
        
        
        
        
solu = Solution()
s = "leetcode"
#s = "loveleetcode"
s = "cc"
print(solu.firstUniqChar(s))