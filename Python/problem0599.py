from typing import List
# from collections import Counter

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        count = len(list1)-1 + len(list2)-1
        # d = Counter(list1)
        d = {}
        for k, s in enumerate(list1):
            d[s] = k
        for k, s in enumerate(list2):
            if s in d:
                if d[s] + k < count:
                    count = d[s] + k
        ans = []
        for k, s in enumerate(list2):
            if s in d:
                if d[s] + k == count:
                    ans.append(s)
        return ans
        

