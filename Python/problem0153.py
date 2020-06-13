# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:14:17 2019

@author: Administrator
"""

class Solution:
    def maxProduct(self, nums: list) -> int:
        if nums == []:
            return []
        MAX = 1
        MIN = 1
        Max = -100000
#        ans = [nums[0]]
        for k in range(0, len(nums)):
            if nums[k] < 0:
                MAX, MIN = MIN, MAX
            MAX = max(nums[k], MAX*nums[k])
            MIN = min(nums[k], MIN*nums[k])
            Max = max(Max, MAX)
#            print(Max)
#            if nums[k] <= MAX*nums[k]:
#                MAX = MAX*nums[k]
#                ans.append(nums[k])
#            else:
#                MAX = nums[k]
#                ans = [nums[k]]
#            if nums[k] <= MAX*nums[k]:
#                MIN = nums[k]
#                ans = [nums[k]]
#                
#            else:
#                MIN = MIN*nums[k]
#                ans.append(nums[k])
        return Max#ans#
        
        
solu = Solution()
nums = [2,3,-2,4]
nums = [-2,0,-1]
#nums = [2,3,-2,4]
nums = [-4,-3,-2]
print(solu.maxProduct(nums))