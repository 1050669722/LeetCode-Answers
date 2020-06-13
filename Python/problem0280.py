# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:48:10 2019

@author: Administrator
"""

class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for k in range(1, len(nums)-1, 2):
            nums[k], nums[k+1] = nums[k+1], nums[k]
        
solu = Solution()
nums = [3,5,2,1,6,4]
solu.wiggleSort(nums)
print(nums)