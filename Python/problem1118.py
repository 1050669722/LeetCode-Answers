# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 09:31:17 2019

@author: ASUS
"""

class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        d = {1:31,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
        if M != 2:
            return d[M]
        if Y % 100 == 0:
            if Y % 400 == 0:
                return 29
            else:
                return 28
        if Y % 4 == 0:
            return 29
        else:
            return 28
        
solu = Solution()
Y, M = 1992, 7
#Y, M = 2000, 2
#Y, M = 1900, 2
print(solu.numberOfDays(Y, M))