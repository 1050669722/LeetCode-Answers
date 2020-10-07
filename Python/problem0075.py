from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # ptr = 0
        # for k in range(len(nums)):
        #     if nums[k] == 0:
        #         nums[ptr], nums[k] = nums[k], nums[ptr]
        #         ptr += 1
        #
        # # ptr = 0
        # for k in range(len(nums)):
        #     if nums[k] == 1:
        #         nums[ptr], nums[k] = nums[k], nums[ptr]
        #         ptr += 1

        # p0, p1 = 0, 0
        # for k in range(len(nums)):
        #     if nums[k] == 1:
        #         nums[p1], nums[k] = nums[k], nums[p1]
        #         p1 += 1
        #
        #     if nums[k] == 0:
        #         nums[p0], nums[k] = nums[k], nums[p0]
        #         if p0 < p1:
        #             nums[p1], nums[k] = nums[k], nums[p1]
        #         p0 += 1
        #         p1 += 1
        #
        #     # print(nums, 'p0: ', p0, ' ', 'p1: ',p1)

        if len(nums) > 1:
            p0, p2 = 0, len(nums) - 1
            k = 0

            while k <= p2:
                # print(nums, p0, p2, k)
                if nums[k] == 2:
                    while nums[k] == 2 and k <= p2:
                        # print(p2, k)
                        nums[p2], nums[k] = nums[k], nums[p2]
                        p2 -= 1

                if nums[k] == 0:
                    nums[p0], nums[k] = nums[k], nums[p0]
                    p0 += 1

                k += 1

            # n = len(nums)
            # p0, p2 = 0, n - 1
            # i = 0
            # while i <= p2:
            #     while i <= p2 and nums[i] == 2:
            #         nums[i], nums[p2] = nums[p2], nums[i]
            #         p2 -= 1
            #     if nums[i] == 0:
            #         nums[i], nums[p0] = nums[p0], nums[i]
            #         p0 += 1
            #     i += 1




solu = Solution()
nums = [2,0,2,1,1,0]
nums = [2,0,1]
nums = [1, 2, 0]
# nums = [2]
# nums = [2,2]
solu.sortColors(nums)
print(nums)
