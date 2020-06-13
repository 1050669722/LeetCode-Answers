class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        for _ in range(K):
            # A.sort()
            A = self.CountSort(A)
            A[0] *= -1
        return sum(A)
    def CountSort(self, nums):
        MIN = min(nums)
        for k in range(len(nums)):
            nums[k] -= MIN
        tmp = [0] * (max(nums)+1)
        for num in nums:
            tmp[num] += 1
        ans = []
        for k in range(len(tmp)):
            for _ in range(tmp[k]):
                ans.append(k)
        for k in range(len(ans)):
            ans[k] += MIN
        return ans
