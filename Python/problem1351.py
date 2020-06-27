class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        g = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                g.append(grid[x][y])
        g.sort(reverse=True)
        i, j = 0, len(g) - 1
        while i < j:
            m = (i + j) // 2
            if g[m] >= 0:
                i = m + 1
            else:
                j = m
        if g[i] >= 0:
            return 0 #特殊的情况，完全没有负数
        return len(g) - i
        
