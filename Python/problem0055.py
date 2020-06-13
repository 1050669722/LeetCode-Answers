# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 16:11:48 2019

@author: Administrator
"""

#class Solution:
#    def canJump(self, nums: list) -> bool:
#        if 0 not in nums:
#            return True
##        if nums == [0]:
##            return True
#        a = []
#        for k in range(len(nums)-1):
#            if nums[k] == 0:
#                a.append(k)
#        Mark = []
#        for p in range(len(a)):
#            if p==0:
#                mark = 0
#                for q in range(0, a[p]):
##                    print(nums[q], a[p]-q)
#                    mark = mark or (nums[q] > a[p]-q)
#                Mark.append(mark)
#            else:
#                if nums[a[p]-1] != 0:
#                    mark = 0
#                for q in range(a[p-1], a[p]):
#                    print(nums[q], a[p]-q)
#                    print('mark', mark)
#                    mark = mark or (nums[q] > a[p]-q)
#                Mark.append(mark)
#        print(Mark)
#        return False not in Mark# and 0 not in Mark
            
class Solution:
   def canJump(self, nums: list) -> bool:
       start = 0
       end = 0
       n = len(nums)
       while start <= end and end < len(nums) - 1: #从每个位置出发（假设的），所能到达的最远处
           end = max(end, nums[start] + start) #每轮得到最远能跳到哪里的索引
           start += 1
       return end >= n - 1
    
#class Solution:
#    def canJump(self, nums: list) -> bool:
#        #start = 0
#        n = len(nums)
#        start = n - 2
#        end = n - 1
#        while start >= 0:
#            if start + nums[start] >= end: end = start
#            start -= 1
#        return end <= 0

#作者：powcai
#链接：https://leetcode-cn.com/problems/two-sum/solution/tan-xin-cong-qian-wang-hou-tiao-cong-hou-wang-qian/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。       
        
class Solution:
   def canJump(self, nums: list) -> bool:
       start = 0
       end = 0
       n = len(nums)
       while start<=end and end<=n-1: #这个等号可以不写
           end = max(end, start+nums[start])
           start += 1
       return end >= n-1
        
solu = Solution()
nums = [2,3,1,1,4]
#nums = [3,2,1,0,4]
nums = [0]
#nums = [2,0,0]
nums = [3,0,0,0]
#nums = [2,0,1,0,1]
print(solu.canJump(nums))