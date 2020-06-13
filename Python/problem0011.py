# -*- coding: utf-8 -*-
"""
Created on Mon May 20 11:21:46 2019

@author: Administrator
"""

#class Solution:
#    def maxArea(self, height: list) -> int:
#        p = 0
#        q = len(height) - 1
#        maxArea = 0
#        while p < q:
#            Area = (q-p) * min(height[p], height[q])
#            if Area <= maxArea:
#                q -= 1
#                Area = (q-p) * min(height[p], height[q])
#                if Area <= maxArea:
#                    p += 1
#                else: 
#                    maxArea = Area
#            else:
#                maxArea = Area
#        return maxArea

#class Solution():
#    def maxArea(self, height: list) -> int:
#        p = 0
#        q = len(height) - 1
#        maxArea = 0
#        while p < q:
#            Area = (q-p) * min(height[p], height[q])
#            if Area <= maxArea:
#                
#                if q == len(height) - 1 or (height[q-1] >= height[q]):
#                    q -= 1
#                else:
#                    q += 1
#                
#                Area = (q-p) * min(height[p], height[q])
#                if Area <= maxArea:
#                    
#                    if p == 0 or (height[p+1] >= height[p]):
#                        p += 1
#                    else:
#                        p -= 1
#                    
#                else: 
#                    maxArea = Area
#            else:
#                maxArea = Area
#        return maxArea

class Solution():#向着面积可能增大的方向移动，以O(n)的时间复杂度遍历，同时伴随着记录；时间复杂度的降低来自于对于更小结果的跳过；已经遍历了所有可能的最大值；用某种办法缩小了搜索空间
    def maxArea(self, height: list) -> int:
        p = 0
        q = len(height) - 1
        maxArea = 0
        while p < q:
            Area = (q-p) * min(height[p], height[q])
            if Area >= maxArea:
                maxArea = Area
            if height[p] <= height[q]:
                p += 1
            else:
                q -= 1
        return maxArea
 
        
solu = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solu.maxArea(height))