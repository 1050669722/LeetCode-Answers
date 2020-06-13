# -*- coding: utf-8 -*-
"""
Created on Sun May 26 21:11:45 2019

@author: Administrator
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
#        for k in range(num):
#            if (k+1)**2 == num:
#                return True
#        return False
        if num == 1:
            return True
        else:
            head, tail = 1, num//2
            while head <= tail:
                mid = (head + tail) // 2
                if mid**2 > num:
                    tail = mid - 1
                elif mid**2 < num:
                    head = mid + 1
                else:
                    return True#mid#
            return False
        
        
        
solu = Solution()
num = 16
#num = 14
num = 151807041
print(solu.isPerfectSquare(num))