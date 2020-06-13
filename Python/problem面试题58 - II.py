class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # a, b = s[:n], s[n:]
        # return b + a
        
        # len_ = len(s)
        # s += s
        # return s[n:n+len_]

        s = list(s)
        s[:n] = reversed(s[:n])
        s[n:] = reversed(s[n:])
        # return ''.join(s)
        return ''.join(reversed(s))

solu = Solution()
s, n = "abcdefg", 2
ans = solu.reverseLeftWords(s, n)
print(ans)