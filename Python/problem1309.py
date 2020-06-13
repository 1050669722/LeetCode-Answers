class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = dict()
        for k in range(1, 10, 1):
            d[str(k)] = chr(96 + k)
        for k in range(10, 27, 1):
            d[str(k)+'#'] = chr(96 + k)

        ans = []
        s = list(s)
        while s:
            tmp = s.pop()
            if tmp == '#':
                tmp1 = s.pop()
                tmp2 = s.pop()
                tmp = tmp2 + tmp1 + tmp
                ans.append(d[tmp])
            else:
                ans.append(d[tmp])
        return ''.join(reversed(ans))

solu = Solution()
s = "10#11#12"
ans = solu.freqAlphabets(s)
print(ans)