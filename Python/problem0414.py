# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:04:26 2019

@author: Administrator
"""

class Solution:
    def thirdMax(self, nums: list) -> int:
        nums = list(set(nums))
        if not nums:
            return None
        if len(nums)<3:
            return max(nums)
        for m in range(3):
            Max = nums[0]
            for k in nums:
                Max = max(Max, k)
            if m != 3-1:
                nums.remove(Max)
            else:
                return Max
        
        
solu = Solution()
nums = [3, 2, 1]
#nums = [1, 2]
nums = [2,2,3,1]
print(solu.thirdMax(nums))