# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 12:47:49 2019

@author: Administrator
"""

class Solution():
    def fun(self, coins, money):
        '''
        给定一些硬币面值coins，需要满足money数，问最少需要几枚硬币。
        '''
        if not coins or min(coins) > money:
            return None
#        if not money:
#            return 0
        dp = [0] * money #这里len(dp)=money已经等于最多的硬币数
        for m in range(money):
            temp = []
            for k in range(len(coins)):
                '''
                最后添加的硬币情况有len(coins)种
                在这些情况里，选择最小的一个
                再添加一个硬币(+1)，就是这一轮的dp
                规定好dp映射含义，输入money，输出最小钱币数
                '''
                # print(money, coins[k])
                if money >= coins[k]:
                    temp.append(dp[m-coins[k]])
#                    dp[m] = min(dp[m], dp[m-coins[k]] + 1)
                # print(temp,'\n')
            dp[m] = min(temp) + 1
#        print(dp)
        return dp[money-1] # money-1 是dp中的最大索引
        
        
        
solu = Solution()
coins = [1,3,4]
#coins = [1,3,5]
money = 6
#money = 0
#money = 2
print(solu.fun(coins, money))