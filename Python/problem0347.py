# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 19:42:21 2019

@author: Administrator
"""

class Solution:
    def topKFrequent(self, nums: list, k: int) -> list:
        d = {}
        for p in range(len(nums)):
            try:
                d[nums[p]] += 1
            except:
                d[nums[p]] = 1
        a = []
        for key, value in d.items():
            a.append((key, value))
        a = sorted(a, key = lambda a: a[1])
#        print(b)
#        print(k)
        b = []
        for _ in range(k):
            b.append( a.pop()[0] )
        return b
        
solu = Solution()
nums, k = [1,1,1,2,2,3], 2
nums, k = [1], 1
print(solu.topKFrequent(nums, k))