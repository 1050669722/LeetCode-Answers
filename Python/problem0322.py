class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        # if amount == 0:
        #     return 0
        # if not coins or amount < min(coins):
        #     return -1
        # if 1 not in coins and amount not in coins and amount%coins[0] != 0:
        #     return -1
        dp = [amount+1] * (amount+1) #0至amount共有amount+1个元素；每一个元素初始化为amount+1，这是对于每个金额至多的硬币数
        dp[0] = 0 #凑出0需要0个硬币
        for m in range(1, amount+1): #边界条件不容易把握
            for coin in coins:
                if m >= coin: #if amount>=coin:也能AC
                    dp[m] = min(dp[m], dp[m-coin] + 1)
        print(dp) #因为硬币的最小面值是1，所以硬币数不应该大于amount
        return dp[amount] if dp[amount] <= amount else -1

solu = Solution()
coins, amount = [1, 2, 5], 11
coins, amount = [2], 3
print(solu.coinChange(coins, amount))
