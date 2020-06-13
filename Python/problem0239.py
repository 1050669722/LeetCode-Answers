# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:28:40 2019

@author: Administrator
"""

class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        if nums == []:
            return []
        if len(nums) <= k:
            return [max(nums)]
        a = []
        for i in range(len(nums)-k+1):
#            print()
#            print(max(nums[i:i+k]))
            a.append(max(nums[i:i+k]))
        return a
        
        
        
        
        
solu = Solution()
nums, k = [1,3,-1,-3,5,3,6,7], 3
nums, k = [1,-1], 1
print(solu.maxSlidingWindow(nums, k))

