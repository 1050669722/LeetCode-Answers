from collections import Counter, defaultdict

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        # print('count: {}'.format(count))
        
        tmp = nums.copy() #list(set(nums.copy()))
        tmp.sort()
        # print('tmp: {}'.format(tmp))
        lastIdx = defaultdict(int)
        for i, num in enumerate(tmp):
            lastIdx[num] = i
        
        smallerThanIt = {}
        for t in tmp:
            smallerThanIt[t] = lastIdx[t] - (count[t] - 1)

        ans = []
        for num in nums:
            ans.append(smallerThanIt[num])

        return ans





