from collections import OrderedDict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1, d2 = OrderedDict(), OrderedDict()
        for k in range(len(s)):
            if s[k] in d1:
                d1[s[k]].append(k)
            else:
                d1[s[k]] = [k]
            if t[k] in d2:
                d2[t[k]].append(k)
            else:
                d2[t[k]] = [k]
        ans1 = [v for v in d1.values()]
        ans2 = [v for v in d2.values()]
        print(ans1, ans2)
        return ans1 == ans2



solu = Solution()
s, t = 'egg', 'add'
print(solu.isIsomorphic(s, t))