from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n % 2 == 1:
            ans = self.sumZero(n-1)
            ans.append(0)
            return ans
        else:
            n //= 2
            ans = []
            for k in range(1, n+1):
                ans.append(k)
                ans.append(-k)
            return ans