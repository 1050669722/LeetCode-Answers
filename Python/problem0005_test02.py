# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         dp = [1] * len(s)
#         for k in range(len(dp)):
#             p, q = k-1, k+1
#             while p >= 0 and q <= len(s)-1:
#                 if s[p] == s[q]:
#                     dp[k] += 2
#                     p -= 1
#                     q += 1
#                 else:
#                     break
#         return max(dp)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        dp = [1] * len(s)
        ans = 1
        res = s[0]
        for k in range(len(dp)):
            # res = s[k]
            p, q = k-1, k+1
            while p >= 0 and q <= len(s)-1:
                if s[p] == s[q]:
                    dp[k] += 2
                    # print(s[p:q+1])
                    # print(dp[k])
                    # print(ans)
                    # print('\n')
                    if dp[k] > ans:
                        ans = dp[k]
                        # print(s[p:q+1])
                        res = s[p:q+1]
                    p -= 1
                    q += 1
                else:
                    break
        res1 = res
        
        dp = [1] * (len(s)-1)
        ans = 2
        res = s[0:2]
        for k in range(len(dp)):
            if s[k] == s[k+1]:
                res = s[k:k+2]
                p, q = k-1, k+1+1
                while p >= 0 and q <= len(s)-1:
                    if s[p] == s[q]:
                        dp[k] += 2
                        # print(s[p:q+1])
                        # print(dp[k])
                        # print(ans)
                        # print('\n')
                        if dp[k] > ans:
                            ans = dp[k]
                            # print(s[p:q+1])
                            res = s[p:q+1]
                        p -= 1
                        q += 1
                    else:
                        break
        res2 = res
        if len(res1) >= len(res2):
            return res1
        else:
            return res2

solu = Solution()
s = "babad"
s = "cbbd"
s = 'ac'
print(solu.longestPalindrome(s))

