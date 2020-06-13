from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for k, num in enumerate(nums):
            if target - num not in d:
                d[num] = k
            else:
                return k, d[target - num]
        return None
