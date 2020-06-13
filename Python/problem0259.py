# -*- coding: utf-8 -*-
"""
Created on Mon May 20 19:43:23 2019

@author: Administrator
"""

class Solution:
    def threeSumSmaller(self, nums: list, target: int) -> int:
#        d = {}
#        for i in range(len(nums)):
#            for j in range(len(nums)):
#                another_num = target - nums[i] - nums[j]
#                if another_num not in d.keys():
#                    d[another_num] = [i, j]
        nums = self.merge_sort(nums)
        ans = 0
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k and j < len(nums):                
#            for j in range(i+1,len(nums)-1):
                if nums[i] + nums[j] + nums[k] < target:
                    ans += k-j
                    j += 1
                else:
                    k -= 1
        return ans
        
    def merge(self, left, right):
        p, q = 0, 0
        result = []
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                result.append(left[p])
                p += 1
            else:
                result.append(right[q])
                q += 1
        result += left[p:]
        result += right[q:]
        return result
        
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
solu = Solution()
nums, target = [-2,0,1,3], 2
print(solu.threeSumSmaller(nums, target))