# class Solution:
#     def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
#         r_idx_mat = list(range(C)) * R
#         c_idx_mat = list(range(R)) * C
#         for r, row in enumerate(r_idx_mat):


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        # # idxes = []
        # # for r in range(R):
        # #     for c in range(C):
        # #         idxes.append([r, c])
        # # idxes = [[r, c] for r in range(R) for c in range(C)]
        # # idxes.sort(key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
        # # return idxes
        # # return sorted(idxes, key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))
        # return sorted([[r, c] for r in range(R) for c in range(C)], key=lambda x: abs(x[0]-r0) + abs(x[1]-c0))

        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        from collections import defaultdict
        bucket = defaultdict(list)
        dist = lambda r1, r2, c1, c2: abs(r1 - r2) + abs(c1 - c2)

        for r in range(R):
            for c in range(C):
                bucket[dist(r, r0, c, c0)].append([r, c])

        ret = list()
        for Dist in range(maxDist + 1):
            ret.extend(bucket[Dist])

        return ret




solu = Solution()
R, C, r0, c0 = 1, 2, 0, 0
R, C, r0, c0 = 2, 2, 0, 1
R, C, r0, c0 = 2, 3, 1, 2
print(solu.allCellsDistOrder(R, C, r0, c0))









