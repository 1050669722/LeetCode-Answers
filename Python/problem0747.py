class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0
        d = {}
        for k in range(len(nums)):
            d[nums[k]] = k
        nums.sort(reverse=True)
        if nums[1] == 0:
            if nums[0] != 0:
                return d[nums[0]]
            else:
                return -1
        if nums[0] >= 2*nums[1]:
            return d[nums[0]]
        else:
            return -1


