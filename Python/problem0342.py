# -*- coding: utf-8 -*-
"""
Created on Sun May 26 20:29:46 2019

@author: Administrator
"""

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while num != 1:
            if num%4 != 0:
                return False
            num //= 4
        return True
        
        return (num>0) and (num & num-1 == 0) and (num & 0x55555555 == 0)
#        return (num>0) and (num & num-1 == 0) and (num & 0b1010101010101010101010101010101 == 0)
#        return num & 0x55555555 == 0
        
        
        
solu = Solution()
num = 16
#num = 5
print(solu.isPowerOfFour(num))