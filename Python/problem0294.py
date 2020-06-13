# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 19:44:28 2019

@author: Administrator
"""

class Solution:
    def canWin(self, s: str) -> bool:
        ans = self.generatePossibleNextMoves(s)
        print(ans)
        count = 0
        for state in ans:
#            print(state)
            for k in range(len(state)-1):
                if state[k:k+2] == '++':
                    count += 1
                    break
#            return True
        if count == len(ans):
            return False
        else:
            return True
        
    def generatePossibleNextMoves(self, s):
        res = []
        for i in range(len(s) - 1):
            if s[i:i+2] == "++":
                res.append(s[:i] + "--" + s[i+2:]) #用到了字符串拼接
        return res
        
        
solu = Solution()
s = "++++"
s = "+++++"
s = "++++++"
print(solu.canWin(s))