class Solution:
    def partitionLabels(self, S: str) -> list:
        d = {}
        for k in range(len(S)):
            d[S[k]] = k
        # print(d)
        # return None
        ans = []
        # while :
        #     p += 1
        FirstInd = 0
        LastInd = 0
        for k in range(len(S)):
            LastInd = max(LastInd, d[S[k]])
            if k == LastInd:#d[S[k]] == LastInd:#
                # ans.append(S[FirstInd:LastInd+1])
                ans.append(len(S[FirstInd:LastInd+1]))
                FirstInd = LastInd+1
        return ans

# solu = Solution()
# S = "ababcbacadefegdehijhklij"
# print(solu.partitionLabels(S))

