from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # count = 0
        # idx1, idx2 = -1, -1
        # max_, idx = nums[0], 0

        # for k in range(1, len(nums)):
        #     if nums[k] < max_:
        #         if count == 0:
        #             idx1 = idx
        #         else:
        #             idx2 = k
        #         count += 1
        #     if nums[k] > max_:
        #         max_, idx = nums[k], k
        
        # # print(idx1, idx2)
        # if idx1 != -1 and idx2 != -1:
        #     return idx2 - idx1 + 1
        # elif idx1 != -1:
        #     return 2
        # else:
        #     return 0


        tmp = sorted(nums)
        count = 0
        idx1, idx2 = -1, -1

        for k in range(len(nums)):
            if tmp[k] != nums[k]:
                if count == 0:
                    idx1 = k
                else:
                    idx2 = k
                count += 1

        if count == 0:
            return 0
        else:
            return idx2 - idx1 + 1

solu = Solution()
nums = [2, 6, 4, 8, 10, 9, 15]
# nums = [1, 2, 3, 4]
# nums = [1, 3, 2, 4]
# nums = [1, 3, 2, 2, 2]
# nums = [2,3,3,2,4]
print(solu.findUnsortedSubarray(nums))