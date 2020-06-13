# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 19:34:31 2019

@author: Administrator
"""

class Solution:
    def findPeakElement(self, nums: list) -> int:
        ans = 0 #可能的索引答案
        before = nums[0] #每轮的前一个数
        for k in range(1, len(nums)):
            if before > nums[k]:
                ans = k-1
                break
            else:
                ans = k
                before = nums[k]
        return ans
        
solu = Solution()
nums = [1,2,3,1]
#nums = [1,2,1,3,5,6,4]
print(solu.findPeakElement(nums))