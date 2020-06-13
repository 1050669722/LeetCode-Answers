# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:25:03 2019

@author: Administrator
"""

class Solution:
    def productExceptSelf(self, nums: list) -> list:
        p = 0
        q = len(nums) - 1
        ans = [1] * len(nums)
        left = 1
        right = 1
        while p < q:
            ans[p] = left * ans[p]
            left = left * ans[p]
            p += 1
            
            ans[q] = right * nums[q]
            right *= ans[q]
            q -= 1
        
        
        
        
        
solu = Solution()
nums = [1,2,3,4]
print(solu.productExceptSelf(nums))