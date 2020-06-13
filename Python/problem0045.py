# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 17:11:08 2019

@author: Administrator
"""

#class Solution:
#    def jump(self, nums: list) -> int:
##        dp = [0] * len(nums)
##        for k in range(1, len(nums)):
##            temp = []
##            for p in range(k):
##                if nums[p] >= k-p:
##                    temp.append(dp[p])
##            dp[k] = min(temp) + 1
##        return dp[-1]
#    
#        n = len(nums)
#        dp = [0] * n
#        for k in range(1, len(nums)):
#            Min = n + 1
#            for p in range(k):
#                if nums[p] >= k-p:
#                    Min = min(dp[p]+1, Min)
#                dp[k] = Min
#        return dp[-1]
        
class Solution:
    def jump(self, nums: list) -> int:
        n = len(nums)
        if n == 1 : 
#            print(dp) 
            return 0
        dp = [0] * n #dp[i]表示,到达该位置已经消耗的最小步数
        for i in range(n): #表示从哪个索引开始
            for j in range(nums[i], 0, -1): #j表示能跳的步长，从远到近
#                print('!')
#                print(i, j)
                if i + j >= n - 1 : 
#                    print(dp) 
                    return dp[i] + 1
                elif dp[i + j] == 0: #能跳到的位置的dp值
                    dp[i + j] = dp[i] + 1
                else:
                    break
        print(dp)
        return "到不了最后"

#作者：powcai
#链接：https://leetcode-cn.com/problems/two-sum/solution/tan-xin-suan-fa-by-powcai/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        
solu = Solution()
nums = [2,3,1,1,4]
print(solu.jump(nums))