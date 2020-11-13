class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # 滑动窗口
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            nums[i] = tmp
        return nums
