class Solution:
    def smallestRangeI(self, A: list, K: int) -> int:
        if not A:
            return 0
        if max(A) - min(A) >= 2*K:
            return max(A) - min(A) - 2*K
        else:
            return 0
        # return max(0, max(A) - min(A) - 2*K)

# solu = Solution()
# A, K = [1], 0
# # A, K = [0, 10], 2
# # A, K = [1, 3, 6], 3
# print(solu.smallestRangeI(A, K))