class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2)+1) for _ in range(len(word1)+1)]
        for p in range(len(word1)+1):
            dp[p][0] = p
        for q in range(len(word2)+1):
            dp[0][q] = q
        for p in range(1, len(word1)+1):
            for q in range(1, len(word2)+1):
                if word1[p-1] == word2[q-1]: #在dp表中引入了空字符格
                    dp[p][q] = 1 + min(dp[p-1][q], dp[p][q-1], dp[p-1][q-1]-1)
                else:
                    dp[p][q] = 1 + min(dp[p-1][q], dp[p][q-1], dp[p-1][q-1])
        return dp[-1][-1]