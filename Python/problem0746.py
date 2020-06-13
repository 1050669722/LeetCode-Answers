# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:57:33 2019

@author: Administrator
"""

class Solution:
    def minCostClimbingStairs(self, cost: list) -> int:
        mark = 0
        if len(cost)%2 == 1:
            mark = 1
        if mark == 0:
            for k in range(1, len(cost))[::-2]:
                if k != len(cost)-1:
                    cost[k-1] = min(cost[k-1]+cost[k-1+2], cost[k-1]+cost[k-1+1]+cost[k-1+1+2])
                    cost[k] = min(cost[k]+cost[k+2], cost[k]+cost[k+1])
#            print(cost)
            return min(cost[0], cost[1])
        else:
            for k in range(2, len(cost))[::-2]:
                if k != len(cost)-1:
                    cost[k-1] = min(cost[k-1]+cost[k-1+2], cost[k-1]+cost[k-1+1]+cost[k-1+1+2])
                    cost[k] = min(cost[k]+cost[k+2], cost[k]+cost[k+1])
            return min(cost[1], cost[2]+cost[0])
        
        
solu = Solution()
cost = [10, 15, 20]
#cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
#cost = [1,0,0,1]
print(solu.minCostClimbingStairs(cost))