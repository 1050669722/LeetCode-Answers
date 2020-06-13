class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                if grid[p][q] > 0:
                    ans += 2
                    # north
                    if p != 0:
                        ans += max(0, grid[p][q]-grid[p-1][q])
                    else:
                        ans += grid[p][q]
                    # south
                    if p != len(grid)-1:
                        ans += max(0, grid[p][q]-grid[p+1][q])
                    else:
                        ans += grid[p][q]
                    # west
                    if q != 0:
                        ans += max(0, grid[p][q]-grid[p][q-1])
                    else:
                        ans += grid[p][q]
                    # east
                    if q != len(grid[0])-1:
                        ans += max(0, grid[p][q]-grid[p][q+1])
                    else:
                        ans += grid[p][q]
        return ans

