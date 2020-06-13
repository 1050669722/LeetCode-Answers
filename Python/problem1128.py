from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # d = {}
        # t = {}
        # for dmn in dominoes:
        #     if (tuple(dmn), tuple(reversed(dmn))) in d:
        #         t[(tuple(dmn), tuple(reversed(dmn)))] += d[(tuple(dmn), tuple(reversed(dmn)))]
        #         d[(tuple(dmn), tuple(reversed(dmn)))] += 1
        #     elif (tuple(reversed(dmn)), tuple(dmn)) in d:
        #         t[(tuple(reversed(dmn)), tuple(dmn))] += d[(tuple(reversed(dmn)), tuple(dmn))]
        #         d[(tuple(reversed(dmn)), tuple(dmn))] += 1
        #     else:
        #         d[(tuple(dmn), tuple(reversed(dmn)))] = 1
        #         t[(tuple(dmn), tuple(reversed(dmn)))] = 0
        #     # print(d, t)
        # # print(t)
        # return sum(t.values())

        d = {}
        # t = {}
        for dmn in dominoes:
            if (tuple(dmn), tuple(reversed(dmn))) in d:
                # t[(tuple(dmn), tuple(reversed(dmn)))] += d[(tuple(dmn), tuple(reversed(dmn)))]
                d[(tuple(dmn), tuple(reversed(dmn)))] += 1
            elif (tuple(reversed(dmn)), tuple(dmn)) in d:
                # t[(tuple(reversed(dmn)), tuple(dmn))] += d[(tuple(reversed(dmn)), tuple(dmn))]
                d[(tuple(reversed(dmn)), tuple(dmn))] += 1
            else:
                d[(tuple(dmn), tuple(reversed(dmn)))] = 1
                # t[(tuple(dmn), tuple(reversed(dmn)))] = 0
            # print(d, t)
        # print(t)
        return sum([sum(range(v)) for v in d.values()])

solu = Solution()
dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[2,1],[1,2],[2,1],[3,4],[5,6]]
print(solu.numEquivDominoPairs(dominoes))


from scipy.special import comb, perm

mark = 1
for k in range(2, 100):
    if comb(k, 2) != sum(range(0, k)):
        mark = 0
        break

print(mark == 1)