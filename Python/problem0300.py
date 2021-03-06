# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 19:37:57 2019

@author: Administrator
"""

class Solution:
    def lengthOfLIS(self, nums: list) -> int:
#        if not nums:
#            return 0
#        d = {}
#        for p in nums:
#            d[p] = []
#            for k, v in d.items():
#                if p > k:
#                    if not d[k]:
#                        d[k].append(p)
#                    elif d[k] and p>d[k][-1]:
#                        d[k].append(p)
#                    elif d[k] and p<d[k][-1]:
#                        d[k].pop()
#                        d[k].append(p)
#        Max = 0
#        for k, v in d.items():
#            Max = max(Max, len(v))
#        print(d)
#        return Max + 1
        
            # 将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例
    # dp 的值： 1  1  1  2  2  3  4    4

#        size = len(nums)
#        # 特判
#        if size <= 1:
#            return size
#        
#        dp = [1] * size
#        for i in range(1, size):
#            for j in range(i):
#                if nums[i] > nums[j]:
#                    # + 1 的位置不要加错了
#                    dp[i] = max(dp[i], dp[j] + 1)
#        # 最后要全部一看遍，取最大值
#        return max(dp)
    
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        
solu = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = []
nums = [1,3,6,7,9,4,10,5,6]
print(solu.lengthOfLIS(nums))