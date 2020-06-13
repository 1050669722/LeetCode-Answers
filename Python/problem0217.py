# -*- coding: utf-8 -*-
"""
Created on Mon May 27 18:01:44 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class Solution:
    def containsDuplicate(self, nums: list) -> bool:
#        d = {}
#        for k in nums:
#            try:
#                d[k] += 1
#            except:
#                d[k] = 1
#        for k, v in d.items():
#            if v >= 2:
#                return True
#        return False
        return len(nums) != len(set(nums))
        
        
solu = Solution()
#nums = [1,2,3,1]
#nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]
#nums = []
for _ in range(10000):
    solu.containsDuplicate(nums)
#    print(solu.containsDuplicate(nums))
    
time2 = time.perf_counter()
print(time2 - time1)