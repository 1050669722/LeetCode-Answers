# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:51:59 2019

@author: Administrator
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
#        Max = 0
        dp = [ [1] * len(s) for _ in range(len(s)) ] #已经包含了中心奇数的情况
        if not s:
            return 0#Max#
        for p in range(len(s)-1): #这里在做中心偶数的情况
            if s[p] == s[p+1]:
                dp[p][p+1] += 1
        for p in range(len(s))[::-1]: #如果len(s) = n, 则list(range(len(s))[::-1])=[n-1, n-2, ..., 0]
            for q in range(p+2, len(s)):
                if s[p] == s[q]:
                    dp[p][q] = dp[p+1][q-1] + 2
                else:
                    dp[p][q] = max(dp[p+1][q], dp[p][q-1])
        print(dp)
        return max(max(dp))
        
solu = Solution()
s = "bbbab"
#s = "cbbd"
print(solu.longestPalindromeSubseq(s))