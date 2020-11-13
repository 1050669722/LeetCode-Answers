import numpy as np
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # nums = np.array(nums)
        # # print(np.tile(nums, (len(nums), 1)))
        # # print(np.tile(nums.reshape(-1, 1), (1, len(nums))))
        # # print(np.tile(nums, (len(nums), 1)) == np.tile(nums.reshape(-1, 1), (1, len(nums))))
        # # print(np.sum(np.tile(nums, (len(nums), 1)) == np.tile(nums.reshape(-1, 1), (1, len(nums)))))
        # return int(np.sum(np.tile(nums, (len(nums), 1)) == np.tile(nums.reshape(-1, 1), (1, len(nums)))) - len(nums)) // 2

        counts, ans = Counter(nums), 0
        for value in counts.values():
            ans += value * (value - 1) // 2
        return ans
        
