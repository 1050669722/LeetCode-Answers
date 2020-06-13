class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2 != 0:
            return False
        factors = [1]
        p, q = 2, num//2
        factors.append(p)
        factors.append(q)
        while p <= q:
            p += 1
            if num % p == 0:
                q = num // p
                if p <= q:
                    factors.append(p)
                    factors.append(q)
            else:
                pass
        return sum(factors) == num

num = 28
num = 36
solu = Solution()
print(solu.checkPerfectNumber(num))