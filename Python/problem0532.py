from typing import List

# class Solution:
#     def findPairs(self, nums: List[int], k: int) -> int:
#         if len(nums) < 2:
#             return 0
#         nums.sort()
#         p, q = 0, 1
#         ans = set()
#         # while p < len(nums):
#         #     if nums[q] - nums[p] == k:
#         #         ans.add((nums[p], nums[q]))
#         #         q = min(q+1, len(nums)-1)
#         #     elif nums[q] - nums[p] < k:
#         #         q = min(q+1, len(nums)-1)
#         #     else:
#         #         p += 1
#         #         q = min(p + 1, len(nums)-1)
#         # return ans
#         while q < len(nums):
#             if nums[q] - nums[p] == k:
#                 ans.add((nums[p], nums[q]))
#                 q += 1
#             elif nums[q] - nums[p] < k:
#                 q += 1
#             else:
#                 p += 1
#                 q = p + 1
#         return len(ans)


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # if len(nums) < 2:
        #     return 0
        if k < 0:
            return 0
        saw, diff = set(), set()
        for num in nums:
            if num - k in saw:
                diff.add(num-k)
            if num + k in saw:
                diff.add(num)
            saw.add(num)
        return len(diff)

        # if k<0:
        #     return 0
        # saw, diff = set(), set()
        # for i in nums:
        #     if i-k in saw:
        #         diff.add(i-k)
        #     if i+k in saw:
        #         diff.add(i)
        #     saw.add(i)
        # return len(diff)

solu = Solution()
nums, k = [3, 1, 4, 1, 5], 2
nums, k = [1, 2, 3, 4, 5], 1
nums, k = [1, 3, 1, 5, 4], 0
print(solu.findPairs(nums, k))