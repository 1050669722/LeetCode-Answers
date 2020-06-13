class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        tmp = []
        while N:
            t = N % 2
            N //= 2
            tmp.append(1-t)
        ans = 0
        for k in range(len(tmp)-1, -1, -1):
            ans += tmp[k] * 2**k
        return ans




