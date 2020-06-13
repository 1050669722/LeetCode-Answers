# -*- coding: utf-8 -*-
"""
Created on Thu May 30 19:58:22 2019

@author: Administrator
"""

class Solution:
    def numSquares(self, n: int) -> int:
        a = []
        self.tempSquares(n, a)
        return a#len(a)#

    def tempSquares(self, x, a):
#        print(x)
        if self.isSquares(x):
            return a.append(x)
#        print(x)
#        print(a)
        for k in range(x, 0, -1):
#            print(k)
            if self.isSquares(k):
                a.append(k)
                x -= k
        self.tempSquares(x, a)
        return
    
    def isSquares(self, m):
        head = 0
        tail = m
#        print(mid)
        while head <= tail:
            mid = (head + tail) // 2
            if mid**2 > m:
                tail = mid - 1
            elif mid**2 < m:
                head = mid + 1
            else:
                return True
#            print(head,tail,mid)
        return head**2 == m or tail**2 == m
        
        
        
solu = Solution()
n = 12
#n = 13
#n = 16
n = 1
#n = 0
n = 2
n = 3
n = 4
n = 5
n = 6
n = 7
n = 8
print(solu.numSquares(n))
#print(solu.isSquares(n))