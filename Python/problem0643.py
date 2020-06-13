class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
            # ans = sum(nums[:k])
            # for i in range(len(nums)-k+1):
            #     ans = max(ans, sum(nums[i:i+k]))
            # return ans/k

            # # nums.sort() # 这是要求子数组，不可能排序
            # # return sum(nums[-4:])/k

            ans = Sum = sum(nums[:k])
            for i in range(k, len(nums)):
                # Sum = Sum - nums[i-k] + nums[i]
                Sum += - nums[i-k] + nums[i]
                ans = max(ans, Sum)
            return ans/k
