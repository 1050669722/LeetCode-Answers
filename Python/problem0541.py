class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        s = list(s)

        for i in range(0, n, 2*k):

            # # tmp = s[i:i+k]
            # if k % 2 != 0:
            #     SpanEnd = i+k//2+1
            #     for j in range(i, SpanEnd-1):
            #         # print(i, j)
            #         s[j], s[SpanEnd-(j-i)] = s[SpanEnd-(j-i)], s[j]
            # else:
            #     SpanEnd = i+k//2
            #     for j in range(i, SpanEnd):
            #         print(i, j)
            #         s[j], s[SpanEnd-(j-i)] = s[SpanEnd-(j-i)], s[j]

            # pre = s[:i]
            # tmp = s[i:i+k]
            # after = s[i+k:]
            # tmp.reverse()
            # # print(pre, tmp, after)
            # s = pre + tmp + after
            # # print(s)

            s[i:i+k] = reversed(s[i:i+k])
            # print(s[i:i + k])

            # s[i:i+k].reverse()
            # print(s[i:i+k])

        return ''.join(s)

solu = Solution()
s, k = "abcdefg", 2
# s, k = "abcdef", 3
# s, k = "ba", 1
# s, k = "abcd", 4
print(solu.reverseStr(s, k))