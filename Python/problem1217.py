from typing import List

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        ans1, ans2 = 0, 0
        for chip in chips:
            if chip %2 == 0:
                ans1 += 1
            else:
                ans2 += 1
        return min(ans1, ans2)

solu = Solution()
chips = [1,2,3]
# chips = [2,2,2,3,3]
print(solu.minCostToMoveChips(chips))