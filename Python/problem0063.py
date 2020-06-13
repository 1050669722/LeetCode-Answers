# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 12:25:03 2019

@author: Administrator
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        a = []
        for _ in range(m):
            a.append([0]*n)
        a[m-1][n-1] = 1 - obstacleGrid[m-1][n-1]
        for k in range(n)[n-2::-1]: #注意list(range(0, -1, -1)) = [0]，所以在列表长度为1时，居然有一轮循环
            if obstacleGrid[m-1][k] == 1:
                a[m-1][k] = 0
            else:
                try:
                    a[m-1][k] = a[m-1][k+1]
                except:
                    pass
        for k in range(m)[m-2::-1]:
            if obstacleGrid[k][-1] == 1:
                a[k][-1] = 0
            else:
                try:
                    a[k][-1] = a[k+1][-1]
                except:
                    pass
        for k in range(m-2, -1, -1): 
            for p in range(n-2, -1, -1):
                if obstacleGrid[k][p] == 1:
                    a[k][p] = 0
                else:
                    a[k][p] = a[k+1][p] + a[k][p+1]
        return a[0][0]
        
solu = Solution()
obstacleGrid = [[0,0,0],
                [0,1,0],
                [0,0,0]]
obstacleGrid = [[1]]
obstacleGrid = [[0]]
print(solu.uniquePathsWithObstacles(obstacleGrid))