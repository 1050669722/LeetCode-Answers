class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        # for i, num in enumerate(nums):
        #     if i == num:
        #         return i
        # return -1

        # i, j = 0, len(nums) - 1
        # while i < j:
        #     m = (i + j) // 2
        #     if nums[m] >= m:
        #         j = m
        #     else:
        #         i = m + 1
        # ans = i if nums[i] == i else -1 #解决不了元素带有重复的问题
        # return ans

        i, j = 0, len(nums)
        while i < j:
            if i == nums[i]:
                return i
            elif i < nums[i]:
                i = nums[i]
            else:
                i += 1
        return -1
