from typing import List
from collections import Counter

# class Solution:
#     def isMajorityElement(self, nums: List[int], target: int) -> bool:
#         d = Counter(nums)
#         return d[target] > len(nums)//2

# class Solution:
#     def isMajorityElement(self, nums: List[int], target: int) -> bool:
#         ans = 0
#         for num in nums:
#             if num == target:
#                 ans += 1
#         return ans > len(target)//2


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        p, q = 0, len(nums)-1
        while p < q:
            if nums[p] > target:
                return False
            elif nums[p] < target:
                p += 1
            if nums[q] < target:
                return False
            elif nums[q] > target:
                q -= 1
            if nums[p] == nums[q] == target:
                return q - p + 1 > len(nums)//2





