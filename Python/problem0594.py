from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        ans = 0
        for key in d:
            if key-1 in d:
                ans = max(ans, d[key]+d[key-1])
        return ans