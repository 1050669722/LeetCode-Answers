from typing import List

class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        d = (arr[-1] - arr[0]) // len(arr)
        if d == 0:
            return arr[0]
        # for k in range(1, len(arr)):
        #     print(arr[k], arr[0] + k*d)
        #     if arr[k] != arr[0] + k*d:
        #         return arr[0] + k*d
        left, right = 0, len(arr)-1
        mid = (left + right) // 2
        while mid != left:
            if arr[mid] - arr[left] == (mid - left) * d:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return arr[mid] + d

solu = Solution()
arr = [1,2,3,5]
arr = [15,13,12]
print(solu.missingNumber(arr))