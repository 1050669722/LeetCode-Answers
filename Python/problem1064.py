# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 20:29:34 2019

@author: Administrator
"""

class Solution:
    def fixedPoint(self, A: list) -> int:
        for k in range(len(A)):
            if k == A[k]:
                return k
        return -1
        
#        dict(zip(, ))
        
solu = Solution()
A = [-10,-5,0,3,7]
print(solu.fixedPoint(A))