class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # nums.sort()
        # for k in range(1, len(nums)):
        #     if nums[k] == nums[k-1]:
        #         # tmp = nums.copy()
        #         return [ nums[k], list( set(range(1, len(nums)+1)) - set(nums) )[0] ]

        d = {}
        for num in nums:
            try:
                d[num] += 1
            except:
                d[num] = 1
        for k, v in d.items():
            if v == 2:
                break
        return [ k, list( set(range(1, len(nums)+1)) - set(nums) )[0] ]



