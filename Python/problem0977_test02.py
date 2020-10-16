class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        p, q = 0, len(A) - 1
        ans = []
        while p <= q:
            if A[p]**2 <= A[q]**2:
                ans.append(A[q]**2)
                q -= 1
            else:
                ans.append(A[p]**2)
                p += 1
        return reversed(ans)
