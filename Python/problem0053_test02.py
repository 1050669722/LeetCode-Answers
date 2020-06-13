class Solution:
    def maxSubArray(self, nums: list) -> int:
        # ans = float('-inf')
        ans = nums[0]
        res = [ans]
        for k in range(1, len(nums)):
            # ans = max(ans, ans+nums[k])
            if ans < 0:
                ans = 0 #如果已经是0了，先变成0，再去加后面的值
            ans += nums[k]
            # print(ans)
            res.append(ans)
        return max(res)

# solu = Solution()
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# print(solu.maxSubArray(nums))
