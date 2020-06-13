# -*- coding: utf-8 -*-
"""
Created on Thu May 30 17:19:26 2019

@author: Administrator
"""

class Solution:
    def maxProfit(self, prices: list) -> int:
#        for p in range(len(prices)):
#            for q in range(p+1,len(prices)):
        if not prices:
            return 0
        max_profit = 0
        min_price = prices[0]
        for k in range(len(prices)):
            if prices[k] < min_price:
                min_price = prices[k]
            if prices[k] - min_price > max_profit:
                max_profit = prices[k] - min_price
        return max_profit
        
solu = Solution()
prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = []
print(solu.maxProfit(prices))