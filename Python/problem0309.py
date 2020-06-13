class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        # if k > len(prices)//2: #以前的超时，只是因为在交易次数足够的情况下仍然当成限制交易次数的情况去处理
        #     pass
            #return self.fun(prices)
        hold = prices[0]
        cash = [0, 0]
        for i in range(1, len(prices)):
            '''
            由于冷冻期的存在，
            如果cash先被赋值的话，
            相当于cash的第一个初始值没有被用到
            '''
            hold = min(hold, prices[i]-cash[0]) #这里必须写cash[0]，因为买的时候，有1天的冷冻期；如果写cash[1]或者max(cash)，则与没有冷冻期的情况没有区别
            cash = [cash[1], max(cash[1], prices[i]-hold)]
        return cash[1]
        # cash = (0, 0)
        # hold = -prices[0]
        # for i in range(1, len(prices)):
        #     '''
        #     这里存在时间顺序上的问题
        #     hold可以在前，或者hold和cash同步，
        #     但是cash不能在前
        #     '''
        #     hold = max(hold, cash[0]-prices[i]) #这里必须写cash[0]，因为买的时候，有1天的冷冻期；如果写cash[1]或者max(cash)，则与没有冷冻期的情况没有区别
        #     cash = (cash[1], max(cash[1], hold+prices[i]))
        # return cash[1]

    # def fun(self, prices):

# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         if not prices:
#             return 0
        
#         # 二、优化
#         maxsell = (0, 0)
#         maxbuy = -1 * prices[0]
#         for i in range(1, len(prices)):
#             maxsell =  (maxsell[1], max(maxsell[1], maxbuy + prices[i]))
#             maxbuy = max(maxbuy, maxsell[0] - prices[i])
#         return maxsell[1] 


