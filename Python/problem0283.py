# -*- coding: utf-8 -*-
"""
Created on Sat May 25 21:20:07 2019

@author: Administrator
"""

class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        p, q = 0, 1
#        for p in range(len(nums)):
#            if nums[p] == 0:
#                for q in range(p+1, len(nums)):
#                    if nums[q] != 0:
#                        nums[p], nums[q] = nums[q], nums[p]
#                        break
        q = 0
        for p in range(len(nums)):
            if nums[p] != 0:
                nums[q] = nums[p] #直接把非零数塞到前面，从而避免了又一重循环
                q += 1
        for k in range(q, len(nums)):
            nums[k] = 0
            k += 1
        
        
        
        
solu = Solution()
nums = [0,1,0,3,12]
#nums = [2,1]
solu.moveZeroes(nums)
print(nums)


#import time
#
#time1 = time.perf_counter()
#for _ in range(1000000):
#    a = [1,2,3,4,5,6,7,8,9,0]
#    while a:
#        a.pop()
#time2 = time.perf_counter()
#print(time2-time1)
#
#time1 = time.perf_counter()
#for _ in range(1000000):
#    a = [1,2,3,4,5,6,7,8,9,0]
#    while a:
#        del a[-1]
#time2 = time.perf_counter()
#print(time2-time1)


