from typing import List

class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        ans = 0
        weight = 0
        for a in arr:
            weight += a
            if weight <= 5000:
                ans += 1
            else:
                break
        return ans