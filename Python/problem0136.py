# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:54:31 2019

@author: Administrator
"""

class Solution:
    def singleNumber(self, nums: list) -> int:
#        d = {}
#        for k in nums:
#            try:
#                d[k] += 1
#            except:
#                d[k] = 1
#        for k, v in d.items():
#            if v == 1:
#                return k
        ans = nums[0]
        for k in nums[1:]:
            ans = ans^k
        return ans
        
solu = Solution()
nums = [2,2,1]
#nums = [4,1,2,1,2]
print(solu.singleNumber(nums))

#交换律：a ^ b ^ c <=> a ^ c ^ b
#
#任何数于0异或为任何数 0 ^ n => n
#
#相同的数异或为0: n ^ n => 0