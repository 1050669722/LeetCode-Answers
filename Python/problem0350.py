from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = Counter(nums2)
        print(d)
        ans = []
        for num in nums1:
            # try:
            #     d[num]
            #     ans.append(num)
            #     print(ans)
            # except:
            #     pass
            # if num in d:
            #     ans.append(num)
            try:
                d[num] -= 1
                if d[num] >= 0:
                    ans.append(num)
            except:
                pass
        return ans

solu = Solution()
nums1, nums2 = [1,2,2,1], [2,2]
nums1, nums2 = [4,9,5], [9,4,9,8,4]
nums1, nums2 = [1,2,2,1], [2]
print(solu.intersect(nums1, nums2))