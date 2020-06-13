# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 10:13:27 2019

@author: Administrator
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        count = 0
        Max = 0
        for k in nums:
            if k == 1:
                count += 1
                Max = max(Max, count)
            else:
                count = 0
        return Max
        
        
solu = Solution()
nus = [1,1,0,1,1,1]
print(solu.findMaxConsecutiveOnes(nums))