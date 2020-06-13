from typing import List

class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        tmp = sorted(nums, reverse=True)
        d = {}
        for k in range(len(tmp)):
            d[tmp[k]] = k
        ans = []
        for num in nums:
            if d[num] == 0:
                ans.append("Gold Medal")
            elif d[num] == 1:
                ans.append("Silver Medal")
            elif d[num] == 2:
                ans.append("Bronze Medal")
            else:
                ans.append(str(d[num]+1))
        return ans
            