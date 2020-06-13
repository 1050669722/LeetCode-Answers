from typing import List

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        mat = [[0]*m for _ in range(n)]
        for ind in indices:
            n, m = ind[0], ind[1]
            mat[n][m] += 1
        ans = 0
        for p in range(len(mat)):
            for q in range(len(mat[0])):
                if mat[p][q] % 2 != 0:
                    ans += 1 
        return ans

n = 2; m = 3; indices = [[0,1],[1,1]]
solu = Solution()
print(solu.oddCells(n, m, indices))