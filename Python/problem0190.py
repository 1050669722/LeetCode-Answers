class Solution:
    def reverseBits(self, n: int) -> int:
        return int(''.join(list(reversed(str(n)))))

solu = Solution()
n = 1
print(solu.reverseBits(n))