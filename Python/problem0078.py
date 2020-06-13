# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:47:54 2019

@author: Administrator
"""

class Solution():
    def __init__(self):
        self.result_all = None
    
    def subsets(self, nums: list) -> list:
#        ans = []
#        for k in range(len(nums)+1):
#            if k == 0:
#                ans.append([])
#            elif k == len(nums):
#                ans.append(nums)
#            else:
#                self.subsets_fun(nums, k)
#        return ans
#                
#    def subsets_fun(self, numsList, element_number):
        self.result_all = []
        self.dfs(nums, 0, 0, [])
        return self.result_all
    
    def dfs(self, nums, n, start, result):
        self.result_all.append(result.copy())
        if n == len(nums):
            return
        else:
            for i in range(start, len(nums)):
                result.append(nums[i])
                self.dfs(nums, n+1, i+1, result)
                result.pop()
            return

solu = Solution()
nums = [1,2,3]
print(solu.subsets(nums))