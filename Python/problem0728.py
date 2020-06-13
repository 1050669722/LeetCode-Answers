# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:22:52 2019

@author: ASUS
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        ans = []
        for k in range(left, right+1):
            if self.isSelfDividingNumber(k) == 1:
                ans.append(k)
        return ans
    def isSelfDividingNumber(self, num):
        List = []
        Num = num
        while num:
            tmp = num%10
            List.append(tmp)
            num //= 10
        if 0 in List:
            return 0
        for n in List:
            if Num % n != 0:
                return 0
        return 1
        
solu = Solution()
left, right = 1, 22
print(solu.selfDividingNumbers(left, right))