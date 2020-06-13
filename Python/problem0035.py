# -*- coding: utf-8 -*-
"""
Created on Thu May 16 11:58:46 2019

@author: Administrator
"""

#class Solution:
#    def searchInsert(self, nums, target):
#        for k in range(len(nums)):
#            if target == nums[k]:
#                return k
#        if target < nums[0]:
#            return 0
#        elif target > nums[-1]:
#            return len(nums)
#        else:
#            mark = 0
#            for k in range(1, len(nums)):
#                temp = mark
#                if target < nums[k]:
#                    mark -= 1
#                if target > nums[k-1]:
#                    mark += 1
#                if mark == temp:
#                    return k

#class Solution():
#    def searchInsert(self, nums, target):
#        for k in range(len(nums)):
#            if nums[k] >= target:
#                return k
#        return k+1 #len(nums)

class Solution():
    def searchInsert(self, nums, target):
        head = 0
        mid = 0
        last = len(nums) - 1
        while(head < last):
            mid = (head+last) // 2#(last - head) // 2 + head #(head+last)/2#
#            print(head)
#            print(last)
#            print(mid)
            if target > nums[mid]:
                head = mid + 1
            elif target < nums[mid]:
                last = mid - 1
            else: 
                return mid
        if target <= nums[last]: #head# #mid是不可以的
            return last #head# #mid是不可以的
        else:
            return last + 1 #head+1# #mid+1是不可以的
     
solu = Solution()
nums, target = [1,3,5,6], 5
nums, target = [1,3,5,6], 2
nums, target = [1,3,5,6], 7
nums, target = [1,3,5,6], 0
#solu.searchInsert(nums, target)
print(solu.searchInsert(nums, target))

