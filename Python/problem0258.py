# -*- coding: utf-8 -*-
"""
Created on Mon May 27 17:03:03 2019

@author: Administrator
"""

class Solution:
    def addDigits(self, num: int) -> int:
#        temp = 10
#        while temp // 10 != 0:
#            temp = 0
#            while num != 0:
#                temp += num % 10
#                num //= 10
#            num = temp
#        return temp
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
        return num
        
solu = Solution()
num = 38
print(solu.addDigits(num))

