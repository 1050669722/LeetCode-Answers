class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp = [1] * len(s)
        # for k in range(len(dp)):
        #     p, q = k-1, k+1
        #     while p >= 0 and q <= len(s)-1:
        #         if s[p] == s[q]:
        #             dp[k] += 2
        #         p -= 1
        #         q += 1

        dp = [ [1] * len(s) for _ in range(len(s)) ] #已经包含了中心奇数的情况
        if not s:
            return 0
        for p in range(len(s)-1): #这里在做中心偶数的情况
            if s[p] == s[p+1]:
                dp[p][p+1] += 1
        for p in range(len(s))[::-1]: #保证每个子问题都已经被遍历到
            for q in range(p+2, len(s)):
                if s[p] == s[q]:
                    dp[p][q] = dp[p+1][q-1] + 2
                else:
                    dp[p][q] = max(dp[p+1][q], dp[p][q-1])
        # print(dp)
        return max([max(x) for x in dp])

solu = Solution()
s = "bbbab"
print(solu.longestPalindromeSubseq(s))





