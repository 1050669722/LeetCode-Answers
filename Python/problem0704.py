# -*- coding: utf-8 -*-
"""
Created on Fri May 31 12:14:15 2019

@author: Administrator
"""

class Solution:
    def search(self, nums: list, target: int) -> int:
        head = 0
        tail = len(nums) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if nums[mid] > target:
                tail = mid - 1
            elif nums[mid] < target:
                head = mid + 1
            else:
                return mid
        return -1
        
solu = Solution()
nums, target = [-1,0,3,5,9,12], 9
#nums, target = [-1,0,3,5,9,12], 2
print(solu.search(nums, target))