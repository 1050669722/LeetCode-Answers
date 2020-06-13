class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        r_idx_mat = list(range(C)) * R
        c_idx_mat = list(range(R)) * C
        for r, row in enumerate(r_idx_mat):


            





solu = Solution()
R, C, r0, c0 = 1, 2, 0, 0
R, C, r0, c0 = 2, 2, 0, 1
R, C, r0, c0 = 2, 3, 1, 2
print(solu.allCellsDistOrder(R, C, r0, c0))









