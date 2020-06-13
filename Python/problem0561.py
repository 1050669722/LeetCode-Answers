# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:19:15 2019

@author: Administrator
"""

class Solution:
    def arrayPairSum(self, nums: list) -> int:
#        nums.sort()
#        Sum = 0
#        for k in range(len(nums)):
#            if k%2 == 1:
#                Sum += min(nums[k], nums[k-1])
#        return Sum
        nums.sort()
        Sum = 0
        for k in range(len(nums)):
            if k%2 == 0:
                Sum += nums[k]
        return Sum
        
        
solu = Solution()
nums = [1,4,3,2]
print(solu.arrayPairSum(nums))