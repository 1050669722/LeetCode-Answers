# -*- coding: utf-8 -*-
"""
Created on Mon May 27 09:57:13 2019

@author: Administrator
"""

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
#        for k in range(c//2+1):
#            if self.isPerfectSquare(k) and self.isPerfectSquare(c-k):
#                return True
#        return False
        p, q = 0, self.isPerfectSquare(c)
        while p <= q:
            if p**2 + q**2 > c:
                q -= 1
            elif p**2 + q**2 < c:
                p += 1
            else:
                return True
        return False
            
    def isPerfectSquare(self, n):
        if n <= 1:
            return True
        head, tail = 2, n//2
        while head <= tail:
            mid = (head + tail) // 2
            if mid**2 > n:
                tail = mid - 1
            elif mid**2 < n:
                head = mid + 1
            else:
                return mid#True#
        return max(head, tail)#False#
        
        
solu = Solution()
n = 5
#n = 3
n = 1000000000
print(solu.judgeSquareSum(n))
