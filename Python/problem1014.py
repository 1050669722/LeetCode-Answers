class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        place_0_value = A[0] + 0
        ans = 0
        for k in range(1, len(A)):
            ans = max(ans, place_0_value + A[k]-k)
            place_0_value = max(place_0_value, A[k]+k)
        return ans
