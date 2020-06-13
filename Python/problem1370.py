class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        d = Counter(s)
        ans = []
        while any(d.values()):
            for letter in sorted(d.keys()):
                if d[letter] != 0:
                    ans.append(letter)
                    d[letter] -= 1
            for letter in reversed(sorted(d.keys())):
                if d[letter] != 0:
                    ans.append(letter)
                    d[letter] -= 1
        return ''.join(ans)

solu = Solution()
s = "aaaabbbbcccc"
ans = solu.sortString(s)
print(ans)