from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m*n
        
        ans = []
        for g in grid:
            for e in g:
                ans.append(e)
        
        tmp = []
        for p in range(len(ans)):
            tmp.append(ans[p-k])
        
        ans = []
        for p in range(0, len(tmp), n):
            ans.append(list(tmp[p:p+n]))

        return ans
