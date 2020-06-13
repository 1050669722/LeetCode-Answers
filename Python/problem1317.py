from typing import List

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for k in range(1, n, 1):
            if ( not self.containZeros(k) ) and ( not self.containZeros(n-k) ):
                return [k, n-k]
    def containZeros(self, num):
        # return '0' in str(num)
        while num:
            tmp = num % 10
            num //= 10
            if tmp == 0:
                return True
        return False

solu = Solution()
n = 1010
print(solu.getNoZeroIntegers(n))