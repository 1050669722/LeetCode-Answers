from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        ans = 0
        max_ = nums[0]
        for num in nums[1:]:
            if num < max_:
                ans += 1
            elif num > max_:
                max_ = num
            # if ans > 1:
            #     return False
        return ans == 1


nums = [4,2,3]
nums = [4,2,1]
solu = Solution()
print(solu.checkPossibility(nums))