# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:38:07 2019

@author: Administrator
"""

class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        self.merge_sort(nums)
#        return nums[-1*k]
        return nums[k-1]
        
    def merge(self, nums, head, mid, tail):
        k = head
        p = head
        q = mid + 1
        temp = nums.copy()
        while p <= mid and q <= tail:
#            if temp[p] <= temp[q]:
            if temp[p] >= temp[q]:
                nums[k] = temp[p]
                k += 1
                p += 1
            else:
                nums[k] = temp[q]
                k += 1
                q += 1
        if p <= mid:
            nums[k:tail+1] = temp[p:mid+1]
        if q <= tail:
            nums[k:tail+1] = temp[q:tail+1]
        
    def merge_sort(self, nums):
        m = 1
        while m < len(nums):
            head = 0
            while head < len(nums):
                mid = head + m - 1
                tail = min(head + 2*m - 1, len(nums) - 1)
                self.merge(nums, head, mid, tail)
                head += 2*m
            m *= 2
        
solu = Solution()
nums, k = [3,2,1,5,6,4], 2
nums, k = [3,2,3,1,2,4,5,5,6], 4
print(solu.findKthLargest(nums, k))
print(nums)