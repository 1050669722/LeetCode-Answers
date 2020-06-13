class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        sum_ori = sum(A)
        for k in range(1, len(A)):
            if A[k] == A[k-1]:
                A[k] += 1
            elif A[k] < A[k-1]:
                A[k] = A[k-1] + 1
        return sum(A) - sum_ori
            


