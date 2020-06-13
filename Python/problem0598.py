from typing import List
from collections import Counter

# class Solution:
#     def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
#         if not m or not n:
#             return None
        
#         mat = [ [0]*n for _ in range(m) ]
#         for op in ops:
#             for p in range(op[0]):
#                 for q in range(op[1]):
#                     mat[p][q] += 1
        
#         mat_ = []
#         for t in mat:
#             mat_ += t
#         # print(mat_)

#         d = Counter(mat_)
#         # print(d)

#         max_ = max(d.keys())
#         # print(list(d.values()))
#         # print(max_)

#         return d[max_]


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m*n
        m, n = ops[0][0], ops[0][1]
        for op in ops:
            m = min(m, op[0])
            n = min(n, op[1])
        return m*n

solu = Solution()
m = 3
n = 3
operations = [[2,2],[3,3]]
print(solu.maxCount(m,n,operations))