# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:55:49 2019

@author: Administrator
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#        if n <= 0:
#            return False
#        while n != 1:
#            if n % 2 != 0:
#                return False
#            n //= 2
#        return True
        
        return n>0 and n & n-1 == 0
        
    def power(self, x, y):
        if y == 0:
            return 1
        if y == 1:
            return x
        temp = self.power(x, y//2)
        if y%2 == 0:
            return temp**2
        else:
            return temp**2*temp
        
        
        
solu = Solution()
n = 1
n = 16
n = 218
print(solu.isPowerOfTwo(n))
print(solu.power(1,2))
print(solu.power(2,3))
print(solu.power(3,4))