class Solution:
    def projectionArea(self, grid: list) -> int:
        ans = 0
        for element in grid:
            ans += max(element)
        # print([0] * len(grid))
        # print(( [0] * len(grid) ) * len(grid[0]))
        grid_copy = [( [0] * len(grid) ) for _ in range(len(grid[0]))]
        # print(grid_copy)
        for p in range(len(grid)):
            for q in range(len(grid[0])):
                # print(p,q)
                grid_copy[q][p] = grid[p][q]
                if grid[p][q] != 0:
                    ans += 1
        for element in grid_copy:
            ans += max(element)
        return ans

# solu = Solution()
# grid = [[1,2],[3,4]]#[[1,2],[3,4],[5,6]]
# print(solu.projectionArea(grid))