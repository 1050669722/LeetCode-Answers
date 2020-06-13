# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 17:03:22 2019

@author: ASUS
"""

class Solution:
    def matrixReshape(self, nums: list, r: int, c: int) -> list:
#        r0, c0 = len(nums), len(nums[0])
#        if r0*c0 != r*c:
#            return nums
#        ans = []
#        for _ in range(r):
#            ans.append([0]*c)
#        tmp = []
#        for p in range(r0):
#            for q in range(c0):
#                tmp.append(nums[p][q])
#        tmp.reverse()
#        for p in range(r):
#            for q in range(c):
#                ans[p][q] = tmp.pop()
#        return ans
        
        r0, c0 = len(nums), len(nums[0])
        if r0*c0 != r*c:
            return nums
        ans = []
        for _ in range(r):
            ans.append([0]*c)
        count = 0
        for p in range(r0):
            for q in range(c0):
                R = count // c
                C = count % c
                count += 1
                ans[R][C] = nums[p][q]
        return ans
        
solu = Solution()
nums, r, c = [[1,2],[3,4]], 1, 4
nums, r, c = [[1,2],[3,4]], 2, 4
print(solu.matrixReshape(nums, r, c))