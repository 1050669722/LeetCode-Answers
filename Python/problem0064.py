# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 18:41:52 2019

@author: Administrator
"""

class Solution:
    def minPathSum(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1:
            return sum(grid[0])
        if n == 1:
            Sum = 0
            for k in grid:
                Sum += k[0]
            return Sum
        for k in range(n)[n-2::-1]:
#            print(-1)
            grid[-1][k] += grid[-1][k+1]
        for k in range(m)[m-2::-1]:
#            print(-2)
            grid[k][-1] += grid[k+1][-1]
#        print(grid)
        for p in range(m-2, -1, -1):
            for q in range(n-2, -1, -1):
                grid[p][q] += min(grid[p][q+1], grid[p+1][q])
#        print(grid)
        return grid[0][0]
                    
        
solu = Solution()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
grid = [[0]]
grid = [[0],[1],[1]]
#grid = [[0, 1, 1]]
print(solu.minPathSum(grid))