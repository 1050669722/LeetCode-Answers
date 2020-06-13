class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        for k in range(1, n+1):
            for p in range(k-1, -1, -1):
                dp[k] += dp[p] * dp[(k-1)-p]
        return dp[n]

# solu = Solution()
# n = 3
# print(solu.numTrees(n))


