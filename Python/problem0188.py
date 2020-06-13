class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        if k > len(prices)//2:
            return self.greedy(prices)
        cash = [[0] * len(prices) for _ in range(k+1)]
        for p in range(1, k+1):
            hold = prices[0]
            for q in range(1, len(prices)):
                cash[p][q] = max(cash[p][q-1], prices[q]-hold)
                hold = min(hold, prices[q]-cash[p-1][q-1])
        return cash[-1][-1]
    
    def greedy(self, prices):
        res = 0
        for i in range(1, len(prices)): #k大于prices长度的一半的时候为什么不用限制交易次数
            if prices[i] > prices[i-1]: #因为这个时候交易次数是足够的
                res += prices[i] - prices[i-1]
        return res


