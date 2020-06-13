# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 16:59:57 2019

@author: ASUS
"""

class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count = 0
        for num in range(L, R+1):
            count += int(self.isRequired(num))
        return count
    def isRequired(self, num):
        count = 0
        while num:
            count += num % 2
            num //= 2
        return self.isPrimeNumber(count)
    def isPrimeNumber(self, count):
        if count == 1:
            return False
        if count == 2:
            return True
        for k in range(2, count):
            if count % k == 0:
                return False
        return True
            
solu = Solution()
L, R = 6, 10
L, R = 10, 15
print(solu.countPrimeSetBits(L, R))