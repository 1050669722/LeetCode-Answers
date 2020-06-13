# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 19:24:21 2019

@author: Administrator
"""

class Solution:
    def repeatedNTimes(self, A: list) -> int:
#        m = 0
#        ans = A[0]
#        for k in range(len(A)):
#            if ans == A[k]:
#                m += 1
#            else:
#                m -= 1
#            if m == -1:
#                m = 0
#                ans = A[k]
#        return ans
        
#        d = {}
#        for k in A:
#            try:
#                d[k] += 1
#            except:
#                d[k] = 1
#        for k, v in d.items():
#            if v == len(A) / 2:
#                return k
        
        for k in range(1, len(A)):
            if A[k] == A[k-1]:
                return A[k]
        if A[0] == A[2]:
            return A[0]
        else:
            return A[-1]
                
        
        
solu = Solution()
A = [1,2,3,3]
#A = [2,1,2,5,3,2]
#A = [5,1,5,2,5,3,5,4]
A = [2,1,0,2]
A = [1,6,6,9]
print(solu.repeatedNTimes(A))