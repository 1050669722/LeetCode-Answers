class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def worker(i, j):
            if grid[i][j] == 1:
                cnt = 0
                if 0 <= i - 1 and grid[i - 1][j] == 1:
                    cnt += 1
                if i + 1 <= m - 1 and grid[i + 1][j] == 1:
                    cnt += 1
                if 0 <= j - 1 and grid[i][j - 1] == 1:
                    cnt += 1
                if j + 1 <= n - 1 and grid[i][j + 1] == 1:
                    cnt += 1
                return 4 - cnt
            else:
                return 0

        ans = 0
        for i in range(m):
            for j in range(n):
                ans += worker(i, j)

        return ans
