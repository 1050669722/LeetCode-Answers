class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        ans1, ans2 = 1, 0
        while n:
            tmp = n % 10
            n //= 10
            ans1 *= tmp
            ans2 += tmp
        return ans1 - ans2
