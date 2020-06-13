# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:43:28 2019

@author: Administrator
"""

class Solution():
    def containsNearbyAlmostDuplicate(self, nums: list, k: int, t: int) -> bool:
        d = {}
        for i in range(len(nums)):
            try:
                if i - d[nums[i]] <= k:
                    return True
                else:
                    d[nums[i]] = i
            except:
                d[nums[i]] = i
        return False
        
        
        
solu = Solution()
nums, k, t = [1,2,3,1], 3, 0
nums, k, t = [1,0,1,1], 1, 2
nums, k, t = [1,5,9,1,5,9], 2, 3
print(solu.containsNearbyAlmostDuplicate(nums, k, t))