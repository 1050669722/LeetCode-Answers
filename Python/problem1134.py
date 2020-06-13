class Solution:
    def isArmstrong(self, N: int) -> bool:
        nums = [int(x) for x in str(N)]
        k = len(nums)
        Sum = sum([x**k for x in nums])
        return Sum == N

