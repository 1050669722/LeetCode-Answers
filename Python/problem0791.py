class Solution:
    def customSortString(self, S: str, T: str) -> str:
        # d = {}
        # for k, s in enumerate(S):
        #     d[s] = k
        # tmp = set(T) - set(S)
        # for t in tmp:
        #     d[t] = -1
        # T = list(T)
        # T.sort(key = lambda x: d[x])
        # T = ''.join(T)
        # return T

        # from collections import Counter
        # d = Counter(T)
        # ans = []
        # tmp = set(T) - set(S)
        # for s in S:
        #     for _ in range(d[s]):
        #         ans.append(s)
        # for t in tmp:
        #     for _ in range(d[t]):
        #         ans.append(t)
        # return ''.join(ans)

        from collections import Counter
        d = Counter(T)
        ans = []
        for s in S:
            ans.append(d[s]*s)
            d[s] = 0
        for e in d:
            ans.append(d[e]*e)
        return ''.join(ans)

S, T = "cba", "abcd"
solu = Solution()
print(solu.customSortString(S, T))