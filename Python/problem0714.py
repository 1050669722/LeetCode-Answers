class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        不限制交易次数，但是有手续费，所以交易次数较少比较好
        这题与前两个股票题不一样，思路上就不一样，这里用到了动态规划
        cash, hold这两个概念比较抽象
        有的动态规划是一个dp，二维
        这里的动态规划是两个dp，都是一维
        '''
        # if not prices:
        #     return 0
        # cash, hold = 0, -prices[0]
        # for k in range(1, len(prices)): #持股相当于负债
        #     cash = max(cash, hold+prices[k]-fee) #对应卖出（卖出需要fee）
        #     hold = max(hold, cash - prices[k]) #对应买入（买入不需要fee）
        # return cash

        if not prices:
            return 0
        cash, hold = 0, prices[0]
        for k in range(1, len(prices)): #持股相当于负债
            '''
            max和min则对应了
            如果不值得
            则
            不卖或不买
            '''
            cash = max(cash, prices[k]-hold-fee) #对应卖出（卖出需要fee）
            hold = min(hold, prices[k]-cash) #对应买入（买入不需要fee）
        return cash






