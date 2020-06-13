# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:09:49 2019

@author: Administrator
"""

#class Solution:
#    def maxSubArray(self, nums):
#        ans = nums[0]
#        for k in range(1, len(nums)+1):
#            for p in range(0, len(nums)):
#                if p+k-1 <= len(nums)-1:
#                    if sum(nums[p:p+k]) > ans:
#                        ans = sum(nums[p:p+k])
#        return ans

#class Solution():
#    def maxSubArray(self, nums):
#        Sum = nums[0]
#        Res = nums[0]
#        for k in range(len(nums)):
#            Sum = max(nums[k], Sum+nums[k])
#            Res = max(Res, Sum)
#        return Res

class Solution:
    def maxSubArray(self, nums: list) -> int:
##        sum_ = 0
#        res = nums[0]
#        p = 0
#        while p<len(nums):
#            sum_ = nums[p]
##            res = max(res, sum_)
#            for q in range(p+1, len(nums)):
#                sum_ += nums[q]
#                res = max(res, sum_)
#                if sum_ <= 0:
##                    p = q# + 1
##                    sum_ = nums[p+1]
##                    res = max(res, sum_)
##                    p = q + 1
##                    try:
##                        sum_ = nums[p]
##                    except:
##                        sum_ = nums[q]
#                    p = q
#                    sum_ = nums[p]
#                    res = max(res, sum_)
#                    break
##                res = max(res, sum_)
#            p += 1
##        print(p,q)
#        return res#q - p + 1#
        
##        sum_ = 0
#        res = nums[0]
#        p = 0
#        while p<len(nums):
#            sum_ = nums[p]
##            res = max(res, sum_)
#            mark = 0
#            for q in range(p+1, len(nums)):
#                sum_ += nums[q]
#                res = max(res, sum_)
#                if sum_ <= 0:
##                    p = q# + 1
##                    sum_ = nums[p+1]
##                    res = max(res, sum_)
##                    p = q + 1
##                    try:
##                        sum_ = nums[p]
##                    except:
##                        sum_ = nums[q]
#                    p = q
#                    sum_ = nums[p]
#                    res = max(res, sum_)
#                    mark = 1
#                    break
##                res = max(res, sum_)
#            if mark != 1:
#                p += 1
##        print(p,q)
#        return res#q - p + 1#
        
        #动态规划 Dynamic Programming
#        Sum = 0
#        ans = nums[0]
#        for k in range(len(nums)):
#            if Sum < 0:
#                Sum = nums[k]
#            else:
#                Sum += nums[k]
#            ans = max(ans, Sum)
#        return ans
        
        #分治法
        n = len(nums)
        if n == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[:n//2])
            max_right = self.maxSubArray(nums[n//2:])
        max_l = nums[n//2-1]
        temp = 0
        for k in range(n//2)[::-1]:
            temp += nums[k] #必须从这一点开始，中间又不能断开
            max_l = max(max_l, temp)
        max_r = nums[n//2]
        temp = 0
        for k in range(n//2, n):
            temp += nums[k]
            max_r = max(max_r, temp)
        return max(max_left, max_right, max_l+max_r)
        

#class Solution:
#    def maxSubArray(self, nums: list) -> int:
#        Sum = 0
#        res = nums[0]
#        for k in range(len(nums)):
#            Sum = max(nums[k], Sum+nums[k]) #舍弃了前面的负和
#            res = max(res, Sum)
#        return res
        

solu = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [1,2,-3,4]
#nums = [-2, 1]
#nums = [-1,0,-2]
print(solu.maxSubArray(nums))


# class Solution:
#     def maxSubArray(self, nums: list) -> int:
#         # ans = float('-inf')
#         ans = nums[0]
#         res = [ans]
#         for k in range(1, len(nums)):
#             # ans = max(ans, ans+nums[k])
#             if ans < 0:
#                 ans = 0
#             ans += nums[k]
#             # print(ans)
#             res.append(ans)
#         return max(res)

# # solu = Solution()
# # nums = [-2,1,-3,4,-1,2,1,-5,4]
# # print(solu.maxSubArray(nums))