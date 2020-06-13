# -*- coding: utf-8 -*-
"""
Created on Thu May 30 11:29:24 2019

@author: Administrator
"""

#class NumArray:
#
#    def __init__(self, nums: list):
#        self.nums = nums
#
#    def sumRange(self, i: int, j: int) -> int:
#        temp = 0
#        for k in range(i, j+1):
#            temp += self.nums[k]
#        return temp

class NumArray:

    def __init__(self, nums: list):
        self.nums = nums
        self.target = []
        Sum = 0
        for k in self.nums:
            Sum += k
            self.target.append(Sum)

    def sumRange(self, i: int, j: int) -> int:
        return self.target[j] - self.target[i] + self.nums[i]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)