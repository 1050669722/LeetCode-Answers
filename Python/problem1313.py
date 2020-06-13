from typing import List

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for k in range(0, len(nums)-1, 2):
            # for _ in range(nums[k]):
            #     ans.append(nums[k+1])
            ans += nums[k] * [nums[k+1]]
        return ans

solu = Solution()
nums = [1,2,3,4]
print(solu.decompressRLElist(nums))