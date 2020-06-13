# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:18:36 2019

@author: Administrator
"""

class Solution:
    def missingNumber(self, nums: list) -> int:
#        if len(nums) <= 1:
#            return None
        try:
            return  list(set(range(len(nums)+1)) - set(nums))[0]
        except:
            return []
        
        
        
        
solu = Solution()
nums = [3,0,1]
#nums = [9,6,4,2,3,5,7,0,1]
nums = [0]
#nums = [0,1]
print(solu.missingNumber(nums))