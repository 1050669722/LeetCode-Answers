from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = {}
        n = len(nums)
        for k in range(1, n+1):
            d[k] = 1
        for num in nums:
            d[num] -= 1
        ans = []
        for k, v in d.items():
            if v == 1:
                ans.append(v)
        return ans