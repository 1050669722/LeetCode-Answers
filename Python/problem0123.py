# class Solution:
#     def maxProfit(self, prices):
#         if not prices:
#             return 0
#         n = len(prices)
#         cash = [[0] * n for _ in range(3)]
#         for k in range(1, 3):
#             hold = prices[0]
#             for i in range(1, n):
#                 cash[k][i] = max(cash[k][i - 1], prices[i] - hold) #现金
#                 hold = min(hold, prices[i] - cash[k - 1][i - 1]) #负债
#         return cash[-1][-1]


class Solution:
    def maxProfit(self, prices):
        '''
        cash[k][i] 为 到第i天经过k次交易得到的最大利润
        '''
        if not prices:
            return 0
        # n = len(prices)
        # cash = [[0] * n for _ in range(3)]
        # for k in range(1, 3):
        #     hold = prices[0]
        #     for i in range(1, n):
        #         cash[k][i] = max(cash[k][i - 1], prices[i] - hold) #现金 #可能的卖出
        #         hold = min(hold, prices[i] - cash[k - 1][i - 1]) #负债 #可能的买入
        
        cash = [ [0] * len(prices) for _ in range(3) ]
        hold = prices[0]
        # print(cash)
        for i in range(1, len(cash)):
            hold = prices[0]
            for k in range(1, len(prices)):
                cash[i][k] = max(cash[i][k-1], prices[k] - hold)
                hold = min(hold, prices[k] - cash[i-1][k-1])

        return cash[-1][-1]
        '''
        有k行的意义在于
        这一次的交易一直在试探，但是并不更新，即本轮不对本轮造成影响
        而是在上一轮的基础上进行规划
        如果本轮对本轮造成影响了，那就是不限制交易次数了
        上一轮的买卖造成的结果，造成的负债hold，来更新这一轮的cash
        '''


