# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 19:18:20 2019

@author: Administrator
"""

class Solution:
    def shortestToChar(self, S: str, C: str) -> list:
        num = []
        for k in range(len(S)):
            if S[k] == C:
                num.append(k)
        
#        tmp = []
#        for k in range(len(num)-1):
#            tmp.append( (num[k] + num[k+1]) // 2 )

        ans = []
        for k in range(len(S)):
            Min = len(S)
            for p in num:
                Min = min(Min, abs(k-p))
            ans.append(Min)
        print(num)
        return ans
        
solu = Solution()
S, C = "loveleetcode", 'e'
print(solu.shortestToChar(S, C))