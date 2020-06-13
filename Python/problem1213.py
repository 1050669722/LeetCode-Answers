from typing import List
from collections import Counter

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # d = Counter(arr1)
        # for a in arr2:
        #     if a in d:
        #         d[a] += 1
        # for a in arr3:
        #     if a in d:
        #         d[a] += 1
        # ans = []
        # for k, v in d.items():
        #     if v == 3:
        #         ans.append(k)
        # return ans

        d = Counter(arr1+arr2+arr3)
        ans = []
        for k, v in d.items():
            if v == 3:
                ans.append(k)
        return ans

        #各数组严格递增排列 => 各数组内部没有重复元素


solu = Solution()
arr1, arr2, arr3 = [1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8]
print(solu.arraysIntersection(arr1, arr2, arr3))