class Solution:
    def tribonacci(self, n: int) -> int:
        ans = [0, 1, 1]
        ans.extend([0]*(n+1-3))
        if n <= 2:
            return ans[n]
        for k in range(3, n+1):
            ans[k] = ans[k-1] + ans[k-2] + ans[k-3]
        return ans[n]

n = 3
# n = 4
# n = 25
solu = Solution()
print(solu.tribonacci(n))