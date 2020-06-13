class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n == 0:
            return 0
        k = 0
        while k * (k+1) <= 2 * n:
            k += 1
        return k-1