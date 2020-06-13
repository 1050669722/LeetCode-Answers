# -*- coding: utf-8 -*-
"""
Created on Thu May 30 12:09:21 2019

@author: Administrator
"""

class Solution:
    def minCost(self, costs: list) -> int:
        if not costs:
            return 0
        cost = costs.copy()
        for i in range(1, len(costs)):
            for j in range(len(costs[i-1])):
                path = costs[i-1][:j] + costs[i-1][j+1:]
                cost[i][j] += min(path) #第i个房子粉刷第j种颜色的累积最小花费
        print(cost)
        print(costs)
        return min(cost[-1])
                
        
        
        
        
        
solu = Solution()
costs = [[17,2,17],[16,16,5],[14,3,19]]
print(solu.minCost(costs))