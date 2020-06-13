# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:59:52 2019

@author: Administrator
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = []
        for _ in range(m):
            a.append([0]*n)
        for k in range(n)[::-1]:
            a[m-1][k] = 1
        for k in range(m)[::-1]:
            a[k][-1] = 1
        for k in range(m-2, -1, -1): 
#        for k in range(0, m-1)[::-1]:# 
#        for k in range(m-1)[::-1]:# 
#        for k in range(m)[m-2::-1]:# 
#        for k in range(m)[m-2:-1:-1]:#
            for p in range(n-2, -1, -1):
                a[k][p] = a[k+1][p] + a[k][p+1]
        return a[0][0]
    
solu = Solution()
m, n = 3, 2
m, n = 7, 3
print(solu.uniquePaths(m, n))