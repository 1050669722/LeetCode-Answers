# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:48:36 2019

@author: Administrator
"""

class Solution():
    def fun(self, A, B):
        '''
        以某一字母结尾
        '''
        if not A or not B:
            return 0
        
        dp = []
        for p in range(len(A)):
            dp.append([0]*len(B))
            
#        if A[0] == B[0]:
#            dp[0][0] = 1
            
        for p in range(0, len(A)):
            if A[p] == B[0]:
                for t in range(p, len(A)):
                    dp[t][0] = 1
                break
        for q in range(0, len(B)):
            if A[0] == B[q]:
                for t in range(q, len(B)):
                    dp[0][t] = 1
                break

        for p in range(1, len(A)):
            for q in range(1, len(B)):
                if A[p] == B[q]:
                    dp[p][q] = dp[p-1][q-1] + 1
                else:
                    dp[p][q] = max(dp[p-1][q], dp[p][q-1]) #+ 1
#        print(dp)
#        return max(max(dp))
        Max = 0
        for p in range(len(dp)):
            for q in range(len(dp[0])):
               Max = max(Max, dp[p][q])
        return Max
        
        
        
        
solu = Solution()
A = 'qwer'
B = 'qdwfegr'
print(solu.fun(A, B))
        