from collections import Counter
from typing import List

# a = [1,2,3,1]
# d = Counter(a)
#
# print(d)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # d = Counter(arr)
        # # print(d)
        # key, value = arr[0], 0
        # for k, v in d.items():
        #     if v > value:
        #         key = k
        #         value = v
        # return key

        n = len(arr)
        current, count = arr[0], 0
        for num in arr:
            if current == num:
                count += 1
                if count * 4 > n:
                    return current
            else:
                current, count = num, 1
        return -1

solu = Solution()
arr = [1,2,2,6,6,6,6,7,10]
print(solu.findSpecialInteger(arr))