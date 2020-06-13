class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list:
        S = A + ' ' + B
        S = S.split()
        # print(A, B)
        # print(S)

        from collections import Counter
        d = Counter(S)
        # print(d)

        # d = {}
        # for s in S:
        #     try:
        #         d[s] += 1
        #     except:
        #         d[s] = 1
        # print(d)

        ans = []
        for key, value in d.items():
            if value == 1:
                ans.append(key)
        return ans

solu = Solution()
A, B = "this apple is sweet", "this apple is sour"
print(solu.uncommonFromSentences(A, B))
