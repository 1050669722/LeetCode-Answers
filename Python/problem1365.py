from typing import List

class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    #     # tmp = nums[:]
    #     # tmp.sort()
    #     tmp = sorted(nums)
    #     # d = {}
    #     d = dict()
    #     # for k in range(len(tmp)):
    #     #     d[tmp[k]] = k
    #     for k, t in enumerate(tmp):
    #         if t not in d:
    #             d[t] = k
    #     ans = []
    #     for num in nums:
    #         ans.append(d[num])
    #     return ans

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # tmp = [0] * len(nums)
        
        # d = dict()
        # for num in nums:
        #     if num not in d:
        #         d[num] = 0
        #     else:
        #         d[num] += 1
        
        # from collections import Counter
        # d = Counter(nums)

        # from collections import OrderedDict
        # from collections import defaultdict
        # d = defaultdict(int)
        # for num in nums:
        #     d[num] += 1

        max_ = max(nums)
        tmp = [0] * (max_+1)
        for num in nums:
            tmp[num] += 1
        # print(tmp)
        
        val = tmp[0]
        for k in range(1, len(tmp)):
            r = tmp[k]
            tmp[k] = val
            val += r
        # print(tmp)
        tmp[0] = 0
        
        ans = []
        for num in nums:
            ans.append(tmp[num])
        return ans

solu = Solution()
nums = [8,1,2,2,3]
nums = [5,0,10,0,10,6]
ans = solu.smallerNumbersThanCurrent(nums)
print(ans)