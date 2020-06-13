from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = [0] * (max(nums)+1)
        for num in nums:
            tmp[num] += 1
        t = []
        for k, tp in enumerate(tmp):
            for _ in range(tp):
                t.append(k)
        # print(t)
        for k in range(len(nums)):
            nums[k] = t[k]
        # return nums

nums = [2,0,2,1,1,0]
solu = Solution()
print(solu.sortColors(nums))