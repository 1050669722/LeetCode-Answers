# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:25:09 2019

@author: Administrator
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
#        if n <= 0:
#            return False
#        while n != 1:
#            if n%3 != 0:
#                return False
#            n //= 3
#        return True
        
        return n>0 and 1162261467%n == 0
        
        
solu = Solution()
n = 27
#n = 0
#n = 9
#n = 45
print(solu.isPowerOfThree(n))