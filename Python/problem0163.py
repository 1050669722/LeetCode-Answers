# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:28:40 2019

@author: Administrator
"""

class Solution:
    def findMissingRanges(self, nums: list, lower: int, upper: int) -> list:
        if len(nums) == 1 and nums[0] == lower:
            return [str(lower+1) + '->' + str(upper)]
        if len(nums) == 1 and nums[0] == upper:
            return [str(lower) + '->' + str(upper-1)]
        if len(nums) == 2 and nums[0] == lower and nums[-1] == upper:
            return []
        a = set(range(lower, upper+1))
        a = list(a - set(nums))
        a = self.summaryRanges(a)
        b = []
        for k in a:
            if type(k) == int:
                b.append(str(k))
            else:
                b.append(str(k[0])+'->'+str(k[-1]))
        return b
        
    def summaryRanges(self, nums: list) -> list:
        if nums == []:
            return nums
        a = [nums[0]]
        for k in range(1, len(nums)):
            if type(a[-1]) != list and nums[k] - a[-1] == 1:
                a.append([a[-1], nums[k]])
                a.pop(-2)
            elif type(a[-1]) == list and nums[k] - a[-1][-1] == 1:
                a.append([a[-1][-1], nums[k]])
            else:
                a.append(nums[k])
        k = -1
        for _ in range(len(a)):
            k += 1
            if k == len(a) - 1: #a[k] == a[-1]:
                break
            if (type(a[k])==list) * (type(a[k+1])==list) == 1:
                if a[k][-1] >= a[k+1][0]:
                    a.insert(k, [a[k][0], max(a[k][-1],a[k+1][-1])])
                    a.pop(k+1)
                    a.pop(k+1)
                    k -= 1
                else:
                    continue
        return a
        
        
        
solu = Solution()
nums, lower, upper = [0, 1, 3, 50, 75], 0, 99,
nums, lower, upper = [], 0, 99,
nums, lower, upper = list(range(0,100)), 0, 99
nums, lower, upper = list(range(0,99)), 0, 99
nums, lower, upper = [2147483647], 0, 2147483647
nums, lower, upper = [-2147483648,2147483647], -2147483648, 2147483647
print(solu.findMissingRanges(nums, lower, upper))