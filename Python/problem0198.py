# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 11:39:52 2019

@author: Administrator
"""

class Solution:
    def rob(self, nums: list) -> int:
#        n = len(nums)
#        if n%2 == 0:
#            m = n//2
#            dp = [0] * m #定义状态
#            dp[0] = max(nums[0], nums[1]) #边界条件
#            for i in range(1, m): #状态转移方程
#                dp[i] = dp[i-1] + max(nums[2*i+1], nums[2*i])
#            print(dp)
#            return dp[-1]
#        else:
#            pass
        
#        if not nums:
#            return 0
#        if len(nums) <= 2:
#            return max(nums)
#        nums_tmp = nums.copy()
#        dp1 = []
#        dp1.append(nums[-1])
#        nums.pop()
#        nums.pop()
#        while nums:
#            if len(nums) <= 2:
#                dp1.append(max(nums))
#                break
#            if nums[-1] >= nums[-2]:
#                dp1.append(nums[-1])
#                nums.pop()
#                nums.pop()
#            else:
#                dp1.append(nums[-2])
#                nums.pop()
#                nums.pop()
#                nums.pop()
#        print(dp1)
#        dp2 = []
#        dp2.append(nums_tmp[-2])
#        nums_tmp.pop()
#        nums_tmp.pop()
#        nums_tmp.pop()
#        while nums_tmp:
#            if len(nums_tmp) <= 2:
#                dp2.append(max(nums_tmp))
#                break
#            if nums_tmp[-1] >= nums_tmp[-2]:
#                dp2.append(nums_tmp[-1])
#                nums_tmp.pop()
#                nums_tmp.pop()
#            else:
#                dp2.append(nums_tmp[-2])
#                nums_tmp.pop()
#                nums_tmp.pop()
#                nums_tmp.pop()
#        print(dp2)
#        return max(sum(dp1), sum(dp2))
        
#        if len(nums) <= 2:
#            return max(nums)
#        dp1 = []
#        dp2 = []
#        dp1.append(nums[0])
#        for k in range(2, len(nums)):
            
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums) #定义状态
        dp[0] = nums[0] #边界条件
        dp[1] = max(nums[:2])
        dp[2] = max(nums[1], nums[0]+nums[2])
#        dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (len(nums)-3)
#        print(dp)
        for k in range(3, len(dp)): #状态转移
            dp[k] = max(dp[k-2], dp[k-3]) + nums[k] #相隔1个，或者相隔2个
#        print(dp)
        return max(dp[-1], dp[-2])#dp[-1]#
        
#        n = len(nums)
#        if n == 0:
#            return 0
#        if n <= 2:
#            return max(nums)
#        i = 3
#        dp = [nums[0]] + [nums[1]] + [nums[0] + nums[2]] + [0] * (n-3)
#        print(dp)
#        while i < n:
#            dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
#            i += 1
#        return max(dp)

#作者：wswsdcc
#链接：https://leetcode-cn.com/problems/two-sum/solution/jian-dan-yi-dong-de-dong-tai-gui-hua-python-by-wsw/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
            
        
solu = Solution()
nums = [1,2,3,1]
#nums = [2,7,9,3,1]
#nums = [2,70,9,2,1]
#nums = []
#nums = [0,0,0]
##nums = [1,2,3]
nums = [6,6,4,8,4,3,3,10]
print(solu.rob(nums))