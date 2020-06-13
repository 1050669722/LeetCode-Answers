from typing import List

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        if len(arr) == 2:
            return [arr]
        min_ = arr[1] - arr[0]
        for k in range(2, len(arr)):
            min_ = min(min_, arr[k]-arr[k-1])
        ans = []
        for k in range(1, len(arr)):
            if arr[k] - arr[k-1] == min_:
                ans.append([arr[k-1], arr[k]])
        return ans

