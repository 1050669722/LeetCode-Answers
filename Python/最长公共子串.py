# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:49:16 2019

@author: Administrator
"""

class Solution():
    def fun(self, a, b):
        '''
        从某一字母开始
        '''
        if not A or not B:
            return 0
        
        dp = []
        for p in range(len(A)):
            dp.append([0]*len(B))
            
        for p in range(0, len(A)):
            if A[p] == B[0]:
                dp[p][0] = 1       
        for q in range(0, len(B)):
            if A[0] == B[q]:
                dp[0][q] = 1

        for p in range(1, len(A)):
            for q in range(1, len(B)):
                if A[p] == B[q]:
                    dp[p][q] = dp[p-1][q-1] + 1
                else:
                    dp[p][q] = 0
        print(dp)
#        return max(max(dp))
        Max = 0
        for p in range(len(dp)):
            for q in range(len(dp[0])):
               Max = max(Max, dp[p][q])
        return Max
        
        
        
        
solu = Solution()
A = 'qwer'
B = 'qdwfegr'
#A = 'q'
#B = 'qd'
print(solu.fun(A, B))