class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            # ans += n % 2
            # n //= 2

            # ans += n & 1
            # n >>= 1

            n &= n - 1
            ans += 1
        return ans

solu = Solution()
n = 0b1011
ans = solu.hammingWeight(n)
print(ans)