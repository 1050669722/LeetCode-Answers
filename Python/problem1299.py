from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_ = arr[-1]
        for k in range(len(arr)-2, -1, -1):
            tmp = max_
            max_ = max(max_, arr[k])
            arr[k] = tmp
        arr[-1] = -1
        return arr

solu = Solution()
arr = [17,18,5,4,6,1]
print(solu.replaceElements(arr))