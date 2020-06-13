# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:02:07 2019

@author: Administrator
"""

class Solution:
    def minimumTotal(self, triangle: list) -> int:
#        Sum, idx = triangle[0][0], 0
#        for k in range(1, len(triangle)):
#            if triangle[k][idx] <= triangle[k][idx+1]:
#                temp = triangle[k][idx]
#            else:
#                idx += 1
#                temp = triangle[k][idx]
#            Sum += temp
#        return Sum
                
#        if len(triangle) == 0:
#            return 0
#        row = len(triangle) - 2
#        for row in range(row, -1, -1):
#            for col in range(len(triangle[row])):
#                triangle[row][col] += min(triangle[row+1][col], triangle[row+1][col+1])
#        return triangle[0][0]
        
        if not triangle:
            return 0
        for p in range(len(triangle)-1)[::-1]:
            for q in range(len(triangle[p])):
                triangle[p][q] += min(triangle[p+1][q], triangle[p+1][q+1])
        return triangle[0][0]
        
solu = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]
print(solu.minimumTotal(triangle))