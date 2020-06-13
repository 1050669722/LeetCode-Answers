# -*- coding: utf-8 -*-
"""
Created on Tue May 21 19:16:36 2019

@author: Administrator
"""

class Solution():
    def __init__(self):
        self.result_all = None
    
    def subsetsWithDup(self, nums: list) -> list:
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
        self.result_all = [[]]
        nums = sorted(nums)
        self.dfs(nums, 0, 0, [])
        return self.result_all
    
    def dfs(self, nums, n, start, result):
        if n == len(nums):
            return
        else:
            pre_num = None
            for i in range(start, len(nums)):
                if nums[i] == pre_num:
                    continue
                pre_num = nums[i] #各层中，以同一数开始的遍历，就不要再做了。排序就是让相同的数都聚到一起
                result.append(nums[i])
                self.result_all.append(result.copy())
                self.dfs(nums, n+1, i+1, result)
                result.pop()
            return
        
solu = Solution()
nums = [1,2,2]
#nums = [4,4,4,1,4]
print(solu.subsetsWithDup(nums))

#AttributeError: 'Solution' object has no attribute 'subsetsWithDup'
#Line 28 in __helper__ (Solution.py)
#Line 42 in _driver (Solution.py)
#Line 53 in <module> (Solution.py)