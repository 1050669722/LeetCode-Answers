# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 20:10:05 2019

@author: Administrator
"""

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        i = 0
        k = 2
        for n in nums:
            if i < k or n != nums[i-k]:
                nums[i] = n
                i += 1
        return nums#i#
    
    
solu = Solution()
nums = [1,1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
print(solu.removeDuplicates(nums))