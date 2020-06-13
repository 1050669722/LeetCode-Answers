# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 18:45:57 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class Solution:
    def findNthDigit(self, n: int) -> int:
#        nums = range(1, 2**31)
#        nums = range(1, n+1)
#        temp1 = [[y for y in str(x)] for x in nums]
#        temp2 = []
#        for p in temp1:
#            temp2 += p
#        return int(temp2[n-1])
        
#        nums = range(1, n+1)
#        temp = []
#        for m in range(len(nums)):
#            t = str(m)
#            for n in range(len(str(m))):
#                temp.append(t[n])
#        return int(temp[n-1])
        
        i = 1
        while True:
            t = 10 ** (i - 1)
            m = i * 9 * t
            if n <= m:
                n -= 1
                return int(str(t + n // i)[n % i])
            n -= m
            i += 1

solu = Solution()
n = 3
#n = 11
n = 10000000
print(solu.findNthDigit(n))

time2 = time.perf_counter()
print(time2 - time1)
        