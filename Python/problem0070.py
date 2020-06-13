# -*- coding: utf-8 -*-
"""
Created on Thu May 23 16:05:33 2019

@author: Administrator
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        a = {}
        a[1] = 1
        a[2] = 2
        for i in range(3, n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]
        
#        if n not in a.keys():
#            a[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
#        return a[n]
        
solu = Solution()
n = 2
n = 3
print(solu.climbStairs(n))