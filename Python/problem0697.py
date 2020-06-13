# -*- coding: utf-8 -*-
"""
Created on Wed May 29 12:00:59 2019

@author: Administrator
"""

class Solution:
    def findShortestSubArray(self, nums: list) -> int:
        d = {}
        for k in range(len(nums)):
            try:
                d[nums[k]].append(k)
            except:
                d[nums[k]] = [k]
        MAX = 0
        mark = nums[0]
        for k, v in d.items():
            if len(v) > MAX:
                MAX = len(v)
                mark = k
            if len(v) == MAX:
                if (d[k][-1]-d[k][0]) < (d[mark][-1]-d[mark][0]):
                    MAX = len(v)
                    mark = k
#        print(MAX)
#        print(mark)
#        print(d)
        return d[mark][-1] - d[mark][0] + 1
        
solu = Solution()
nums = [1, 2, 2, 3, 1]
#nums = [1,2,2,3,1,4,2]
print(solu.findShortestSubArray(nums))