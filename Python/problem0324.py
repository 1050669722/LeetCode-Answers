# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:59:43 2019

@author: Administrator
"""

class Solution:
    def wiggleSort(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        nums.sort()
#        if len(nums) % 2 == 0:
#            nums[::2], nums[1::2] = nums[:len(nums)//2], nums[len(nums)//2:]
#        else:
#            nums[::2], nums[1::2] = nums[:len(nums)//2+1], nums[len(nums)//2+1:]
        
#        nums.sort(reverse=True)
#        nums[::2], nums[1::2] = nums[len(nums)//2:], nums[:len(nums)//2]
        
        nums.sort()
        half = len(nums[::2])
        nums[::2], nums[1::2] = nums[:half][::-1], nums[half:][::-1]
#        nums[::2], nums[1::2] = nums[:half], nums[half:]
        
        
solu = Solution()
nums = [1, 5, 1, 1, 6, 4]
nums = [1, 3, 2, 2, 3, 1]
#nums = [1, 1, 2, 1, 2, 2, 1]
nums = [4,5,5,6]
solu.wiggleSort(nums)
print(nums)