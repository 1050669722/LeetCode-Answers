from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        # # d = {}
        # # for k, num in enumerate(nums):
        # #     if num < 0:
        # #         d[num] = 1
        # #     else:
        # #         d[num] = 0
        # # nums.sort(reverse = True, key = lambda x: abs(x))
        # # print(nums)
        # # for k in range(0, len(nums)-2):
        # #     if (d[nums[k]] + d[nums[k+1]] + d[nums[k+2]]) % 2 == 0:
        # #         return nums[k] * nums[k+1] * nums[k+2]
        # nums.sort(reverse = True)
        # tmp1 = nums[0] * nums[1] * nums[2]
        # tmp2 = nums[0] * nums[-1] * nums[-2]
        # # print(nums)
        # return max(tmp1, tmp2)

        max1, max2, max3 = 0, 0, 0#nums[0], nums[0], nums[0]
        min1, min2 = 0, 0#nums[0], nums[0]
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        # print(max1, max2, max3, min1, min2)
        return max(max1 * max2 * max3, max1 * min1 * min2)

solu = Solution()
ans = solu.maximumProduct([3, -2, 2, -1, 1])
print(ans)