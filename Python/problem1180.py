# class Solution:
#     def countLetters(self, S: str) -> int:
#         if not S:
#             return 0
#         ans = 0
#         for p in range(len(S)):
#             for q in range(p, len(S)):
#                 tmp = S[p:q+1]
#                 if len(set(tmp)) == 1:
#                     # print(tmp)
#                     ans += 1
#         return ans

# # solu = Solution()
# # S = "aaaba"
# # print(solu.countLetters(S))


class Solution:
    def countLetters(self, S: str) -> int:
        p, q = 0, 0
        ans = 0
        while q <= len(S)-1:
            if S[q] == S[p]:
                q += 1
            else:
                n = q - p
                p = q
                ans += self.fun(n)
        return ans + self.fun(q - p)

    def fun(self, n):
        return (n+1) * n // 2


solu = Solution()
S = "aaaba"
S = "aaaaaaaaaa"
print(solu.countLetters(S))