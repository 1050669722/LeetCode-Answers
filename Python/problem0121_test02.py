# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         '''
#         这无非就是在找两个最值
#         这两个最值是有依赖关系的
#         '''
#         minprice = float('inf')
#         maxprofit = 0
#         for k in range(len(prices)):
#             if prices[k] < minprice:
#                 minprice = prices[k]
#             elif prices[k] - minprice > maxprofit: #两重可能的身份，如果这个价格不是最低价格，那么它有可能带来最大利润
#                 maxprofit = prices[k] - minprice
#         return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cash = [[0] * len(prices) for _ in range(2)]
        hold = prices[0]
        for p in range(1, 2):
            for q in range(1, len(prices)):
                cash[p][q] = max(cash[p][q-1], prices[q]-hold)
                hold = min(hold, prices[q]-cash[p-1][q-1]) #p-1意味着在那个时候，那个时候是还没有进行本次交易的时候
        print(cash[-1][-1])