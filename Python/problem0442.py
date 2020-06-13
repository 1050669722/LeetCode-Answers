# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:24:34 2019

@author: Administrator
"""

class Solution:
    def findDuplicates(self, nums: list) -> list:
#        Sum = 1
#        k = 0
#        while Sum:
#            Sum ^= nums[k]
#            if Sum == 0:
#            k += 1
        
#        d = {}
#        for k in nums:
#            try:
#                d[k] += 1
#            except:
#                d[k] = 1
#        ans = []
#        for k, v in d.items():
#            if v == 2:
#                ans.append(k)
#        return ans
    
        res = []
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num-1] > 0: #1<= a[i] <= n
                nums[num-1] *= -1
            else:
                res.append(num)
        return res
        
solu = Solution()
nums = [4,3,2,7,8,2,3,1]
print(solu.findDuplicates(nums))