# -*- coding: utf-8 -*-
"""
Created on Fri May 17 10:34:43 2019

@author: Administrator
"""

class Solution():
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums = self.merge_sort(nums)
        closest= nums[0] + nums[1] + nums[2]
        for k in range(len(nums)): #for在内部迭代出最近目标或直接找到目标返回，没有在内部返回，说明没有目标值，只能跳出，然后在外部返回最近目标
            p = k + 1
            q = len(nums) - 1
            while p < q: 
#                if nums[k]+nums[p]+nums[q] < target: #
#                    if abs((nums[k]+nums[p]+nums[q])-target) < abs(closest-target):
#                        closest = nums[k]+nums[p]+nums[q]
#                    p += 1
#                elif nums[k]+nums[p]+nums[q] > target:
#                    if abs((nums[k]+nums[p]+nums[q])-target) < abs(closest-target):
#                        closest = nums[k]+nums[p]+nums[q]
#                    q -= 1
#                else:
#                    return closest
                if abs((nums[k]+nums[p]+nums[q])-target) < abs(closest-target):
                    closest = nums[k]+nums[p]+nums[q]
                if nums[k]+nums[p]+nums[q] < target:
                    p += 1
                elif nums[k]+nums[p]+nums[q] > target:
                    q -= 1
                else:
                    return nums[k]+nums[p]+nums[q]
        return closest
        
    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i<len(left) and j<len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result += left[i:]
        result += right[j:]
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
#nums, target = [-1, 2, 1, -4], 1
#nums, target = [0,2,1,-3], 1
nums, target = [1,1,-1,-1,3], 1
print(solu.threeSumClosest(nums, target))
print(solu.merge_sort(nums))













