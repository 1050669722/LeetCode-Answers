from typing import List

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        OddInEvenInds, EvenInOddInds = [], []
        for k in range(0, len(A), 2):
            if A[k]%2 == 1:
                OddInEvenInds.append(k)
        for k in range(1, len(A), 2):
            if A[k]%2 == 0:
                EvenInOddInds.append(k)
        for i in range(len(OddInEvenInds)):
            A[OddInEvenInds[i]], A[EvenInOddInds[i]] = A[EvenInOddInds[i]], A[OddInEvenInds[i]]
        return A




