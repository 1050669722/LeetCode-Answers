from typing import *
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        ans = []

        for first in range(0, len(nums), 1): #因为数组是排好序的，所以没有出现重复
            if nums[first] == nums[first - 1] and first > 0:
                continue

            for second in range(first + 1, len(nums), 1):
                if nums[second] == nums[second - 1] and second > first + 1:
                    continue

                fourth = len(nums) - 1

                for third in range(second + 1, len(nums), 1):
                    if nums[third] == nums[third - 1] and third > second + 1:
                        continue

                    while third < fourth and nums[first] + nums[second] + nums[third] + nums[fourth] > target:
                        fourth -= 1

                    if third == fourth:
                        break
                    if nums[first] + nums[second] + nums[third] + nums[fourth] < target:
                        continue
                    if nums[first] + nums[second] + nums[third] + nums[fourth] == target:
                        ans.append([nums[first], nums[second], nums[third], nums[fourth]])

        return ans
