from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # # for k, num in enumerate(nums):
        # #     nums[k] = a*num**2 + b*num + c
        # nums = list(map(lambda x: a*x**2 + b*x + c, nums))
        
        # min_ = min(nums)
        # nums = [num-min_ for num in nums]
        # max_ = max(nums)
        # tmp = [0] * (max_+1)
        # # print(nums)
        # for num in nums:
        #     tmp[num] += 1
        
        # nums = []
        # for k, t in enumerate(tmp):
        #     for _ in range(t):
        #         nums.append(k)
        # nums = list(map(lambda x: x+min_, nums))
        
        # return nums

        nums = list(map(lambda x: a*x**2 + b*x + c, nums))
        return sorted(nums)


# nums = [-4,-2,2,4]; a = 1; b = 3; c = 5
nums = [-99,-98,-94,-92,-87,-82,-71,-62,-57,-57,-45,-39,-36,-23,-21,-14,-3,3,12,12,16,19,27,27,28,41,47,51,52,60,70,77,78,88]
a = -34
b = 96
c = -67
solu = Solution()
print(solu.sortTransformedArray(nums, a, b, c))