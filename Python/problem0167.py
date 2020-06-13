# -*- coding: utf-8 -*-
"""
Created on Thu May 16 21:24:36 2019

@author: Administrator
"""

class Solution():
    def twoSum(self, numbers: list, target: int) -> list:
        if len(numbers) <= 1:
            return [None, None]
        else:
            p = 0
            q = len(numbers) - 1
            while p < q:
                if numbers[p] + numbers[q] < target:
                    p += 1
                elif numbers[p] + numbers[q] > target:
                    q -= 1
                else:
                    return [p+1, q+1]
            return [None, None]
        
solu = Solution()
numbers, target = [2, 7, 11, 15], 9
print(solu.twoSum(numbers, target))