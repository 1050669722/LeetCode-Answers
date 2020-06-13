from typing import List

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        letter = S[0]
        start = 0
        count = 1
        d = {}
        for k in range(1, len(S)):
            if S[k] == letter:
                count += 1
            else:
                letter = S[k]
                start = k
                count = 1
            if count >= 3:
                d[(start, letter)] = [start, k]
            # print(count)
            # print(d)
        return list(d.values())


        # d = {}
        # for k, s in enumerate(S):
        #     if s in d and k - d[s][-1] == 1:
        #             d[s].append(k)
        #     else:
        #         d[s] = [k]
        # print(d)
        # ans = []
        # # for k, v in d.items():
        # for v in d.values():
        #     if len(v) >= 2 and v[-1] - v[0] > 2:
        #         ans.append([v[0], v[-1]])
        # return ans

solu = Solution()
S = "abcdddeeeeaabbbcd"
S = 'aaa'
S = "nnnhaaannnm"
print(solu.largeGroupPositions(S))