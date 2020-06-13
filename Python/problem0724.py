from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        tmp = 0
        for k, num in enumerate(nums):
            if k > 0:
                tmp += nums[k-1]
            if 2*tmp == sum_ - num:
                return k
        return -1