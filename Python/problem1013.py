from typing import List

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_ = sum(A)
        tmp = sum_//3
        if 3*tmp != sum_:
            return False
        sum_ = 0
        mark = 0
        for a in A:
            sum_ += a
            if sum_ == tmp:
                sum_ = 0
                mark += 1
        return mark == 3

solu = Solution()
A = [0,2,1,-6,6,-7,9,1,2,0,1]
A = [0,2,1,-6,6,7,9,-1,2,0,1]
# A = [3,3,6,5,-2,2,5,1,-9,4]
print(solu.canThreePartsEqualSum(A))