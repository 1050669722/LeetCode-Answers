class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2 or sum(nums) % 2 != 0 or max(nums) > sum(nums) // 2:
            return False

        dp = [[False] * (sum(nums) // 2 + 1) for _ in range(len(nums))]
        # print(dp)

        for i in range(len(dp)):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1, len(dp)):
            for j in range(len(dp[0])):
                if dp[i - 1][j] == True:
                    dp[i][j] = True
                elif j >= i: #j代表target逐渐值，如果target比较大，则i增大的时候，尚有可能取得target；但是如果target比较小，则增大i，更不可能取得target；
                    dp[i][j] = dp[i - 1][j - nums[i]]
        # print(dp)

        return dp[-1][-1] #注意，并没有将nums排序
                    
