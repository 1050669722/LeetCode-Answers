from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        for a in arr:
            if a in d:
                d[a] += 1
            else:
                d[a] = 1
        return len(list(d.values())) == len(set(d.values()))