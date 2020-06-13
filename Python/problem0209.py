# -*- coding: utf-8 -*-
"""
Created on Tue May 21 20:48:22 2019

@author: Administrator
"""

class Solution:
    def minSubArrayLen(self, s: int, nums: list) -> int:
#       if nums == []:
#           return 0
#       nums = sorted(nums)
#       nums.reverse()
#       ans = 0
#       for i in range(len(nums)):
#           k = len(nums) - 1
#           j = i + 1
#           while j < k:
#               if 
        ans = len(nums)+1
        p, q = 0, 0
        summ = 0
#        print(nums)
        while q < len(nums):
            if summ < s:
                summ += nums[q]
                q += 1
#            print(summ)
#            print('---')
#            print(ans)
            while p < q and summ >= s:
#                print(-1)
#            elif p < q: #这两句话在这里并不等价，注意这里while表示又是一个小循环
                ans = min(q - p, ans)
                summ -= nums[p]
                p += 1
#        print(p)
#        print(q)
        return ans if ans != len(nums)+1 else 0
        
solu = Solution()
#nums, s = [2,3,1,2,4,3], 7
#print(nums)
nums, s = [1,1], 3
print(solu.minSubArrayLen(s, nums))