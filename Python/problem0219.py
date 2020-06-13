# -*- coding: utf-8 -*-
"""
Created on Tue May 28 12:08:06 2019

@author: Administrator
"""

class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
#        if len(nums)<=1:
#            return False
#        for p in range(len(nums)):
#            for q in range(p-k, p+k+1):
#                if q>=len(nums):
##                    print(-1)
#                    q = len(nums)-1#q -= len(nums)
#                if q<0:#if q<=-len(nums):#if q<-len(nums):
##                    print(-2)
#                    q = 0#q += len(nums)
#                if q!=p and nums[q] == nums[p]:
##                    print(-3)
##                    print(q,p)
#                    return True
#        return False
        
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
nums, k = [1,2,3,1], 3
#nums, k = [1,0,1,1], 1
#nums, k = [1,2,3,1,2,3], 2
nums, k = [2,2], 3
#nums, k = [1], 1
#nums, k = [1,2], 2
nums, k = [1,2,3,1,2,3], 2
print(solu.containsNearbyDuplicate(nums, k))