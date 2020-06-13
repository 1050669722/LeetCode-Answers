# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:46:06 2019

@author: Administrator
"""

class Solution:
    def lengthOfLIS(self, nums: list) -> int:
        '''
        从开始到最后，
        遍历每一个字母，
        以每一个字母为子序列末尾字母，
        动态规划，
        状态
        和
        状态方程
        '''
#        if not nums:
#            return 0
#        dp = [1] * len(nums)
#        for p in range(1, len(nums)):
#            temp = [0]
#            for q in range(p):
##                print(p,q)
##                print(dp[p],dp[q])
#                if nums[p] > nums[q]:
##                    print(-1)
#                    temp.append(dp[q])
##            print(temp)
#            dp[p] = max(temp) + 1
##        print(dp)
#        return max(dp)
    
        if not nums:
            return 0
        dp = [1] * len(nums)
        for p in range(1, len(nums)):
            for q in range(p):
                if nums[p] > nums[q]:
                    dp[p] = max(dp[p], dp[q]+1)
        return max(dp)
                
        
solu = Solution()
nums = [10,9,2,5,3,7,101,18]
nums = []
nums = [1,3,6,7,9,4,10,5,6]
print(solu.lengthOfLIS(nums))