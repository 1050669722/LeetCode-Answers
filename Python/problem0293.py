# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:34:04 2019

@author: Administrator
"""

class Solution:
    def generatePossibleNextMoves(self, s: str) -> list:
        ans = []
        tmp = list(s)
        for k in range(len(tmp)-1):
            if tmp[k] == '+' and tmp[k+1] == '+':
                tmp[k] = '-'
                tmp[k+1] = '-'
                ans.append(''.join(tmp))
                tmp = list(s)
        return ans

    
#class Solution(object):
#    def generatePossibleNextMoves(self, s):
#        """
#        :type s: str
#        :rtype: List[str]
#        """
#        res = []
#        for i in range(len(s) - 1):
#            if s[i:i+2] == "++":
#                res.append(s[:i] + "--" + s[i+2:])
#        return res
        
        
        
solu = Solution()
s = "++++"
print(solu.generatePossibleNextMoves(s))