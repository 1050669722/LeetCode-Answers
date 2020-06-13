class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # if not s:
        #     return 0
        # if s == '()':
        #     return 2
        # maxans = 0
        # dp = [0] * len(s)
        # if s[:2] == '()':
        #     dp[1] = 2
        # for k in range(2, len(s)):
        #     if s[k] == ')':
        #         if s[k-1] == '(':
        #             dp[k] = dp[k-2] + 2
        #         else:
        #             if k-1-dp[k-1]>=0 and s[k-1-dp[k-1]] == '(':
        #                 if k-1-dp[k-1]-1 >= 0:
        #                     dp[k] = dp[k-1] + dp[k-1-dp[k-1]-1] + 2
        #                 else:
        #                     dp[k] = dp[k-1] + 0 + 2
        #     maxans = max(maxans, dp[k])
        # # print(dp)
        # return maxans#max(dp)#

        maxans = 0
        dp = [0] * len(s)
        for k in range(1, len(s)):
            if s[k] == ')':
                if s[k-1] == '(':
                    if k-2 >= 0:
                        dp[k] = dp[k-2] + 2
                    else:
                        dp[k] = 0 + 2
                elif k-dp[k-1]-1 >= 0 and s[k-dp[k-1]-1] == '(':
                    if k-dp[k-1]-2 >= 0:
                        dp[k] = dp[k-1] + dp[k-dp[k-1]-2] + 2
                    else:
                        dp[k] = dp[k-1] + 0 + 2
                maxans = max(maxans, dp[k])
        return maxans

solu = Solution()
s = "(()"
# s = ")()())"
print(solu.longestValidParentheses(s))
