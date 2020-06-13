# -*- coding: utf-8 -*-
"""
Created on Sat May 25 20:07:09 2019

@author: Administrator
"""

class Solution:
    def majorityElement(self, nums: list) -> int:
##        d = {}
##        for k in nums:
##            try:
##                d[k] += 1
##            except:
##                d[k] = 1
##        for k, v in d.items():
##            if v > len(nums)/2:
##                return k
#        
#        if len(nums) == 0:
#            return None
#        if len(nums) == 1:
#            return nums[0]
#        nums = sorted(nums)
##        nums = self.merge_sort(nums)
##        print(self.merge_sort(nums))
##        nums = sorted(nums)
##        print(nums)
##        a = 1
##        for k in range(1, len(nums)):
##            if nums[k] != nums[k-1]:
##                a = 1
##            else:
##                a += 1
##                if a > len(nums)/2:
##                    return nums[k]
##        return None
        
#        return nums[len(nums)//2]
        
        count = 1
        ans = nums[0]
        for k in range(1, len(nums)):
            if nums[k] == ans:
                count += 1 #大于一半长度，统计个数
            else:
                count -= 1 #消耗个数，扛消耗
                if count == 0:
                    ans = nums[k+1] #这个时候count已经为0了，所以要写k+1
        return ans
    
    def merge(self, left, right):
        p, q = 0, 0
        ans = []
        while p<len(left) and q<len(right):
            if left[p] <= right[q]:
                ans.append(left[p])
                p += 1
            else:
                ans.append(right[q])
                q += 1
        ans += left[p:]
        ans += right[q:]
        return ans
        
    def merge_sort(self, List):
        if len(List) <= 1:
            return List
        else:
            num = len(List) // 2
            left = self.merge_sort(List[:num])
            right = self.merge_sort(List[num:])
            return self.merge(left, right)
        
solu = Solution()
nums = [3,2,3]
#nums = [2,2,1,1,1,2,2]
#nums = [1]
#nums = []
###nums = [2,2,1,1,4,2,3]
print(solu.majorityElement(nums))
#print(solu.merge_sort(nums))