from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        max_, length = 1, 1
        for k in range(1, len(nums)):
            if nums[k] > nums[k-1]:
                length += 1
            else:
                max_ = max(max_, length)
                length = 1
        max_ = max(max_, length)
        return max_

nums = [1,3,5,4,7]
# nums = [2,2,2,2,2]
nums = [1,3,5,7]
solu = Solution()
print(solu.findLengthOfLCIS(nums))