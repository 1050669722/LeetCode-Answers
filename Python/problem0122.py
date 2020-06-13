# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         '''
#         兴趣点在于连续的谷和峰，这样中间就没有折腾
#         循环寻找相邻的谷和峰，外层的一轮循环就是一对谷和峰
#         找到正确的方法是关键，事半功倍，四两拨千斤
#         '''
#         maxprofit = 0
#         if not prices:
#             return maxprofit
#         valley = prices[0]
#         peak = prices[0]
#         k = 0
#         while(k<len(prices)-1):
#             while(k<len(prices)-1 and prices[k] >= prices[k+1]):
#                 k += 1
#             valley = prices[k]
#             while(k<len(prices)-1 and prices[k] <= prices[k+1]): # 峰要在谷的后面找
#                 k += 1
#             peak = prices[k]
#             maxprofit += peak - valley
#         return maxprofit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        和上面是等价的
        相邻谷峰值转化为相邻低高点
        '''
        maxprofit = 0
        if not prices:
            return maxprofit
        for k in range(1, len(prices)):
            if prices[k] > prices[k-1]:
                maxprofit += prices[k] - prices[k-1]
        return maxprofit


