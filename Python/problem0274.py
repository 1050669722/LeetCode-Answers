from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        if set(citations) == {0}:
            return 0

        # citations.sort(reverse = True)
        # for k, citation in enumerate(citations):
        #     if citation <= k+1:
        #         return citations.count(citation)
        # return len(citations)

        citations.sort(reverse = True)
        d = {}
        d[citations[0]] = 1
        for k in range(1, len(citations)):
            if citations[k] in d:
                d[citations[k]] += 1
                tmp = d[citations[k]]
            else:
                d[citations[k]] = k+1
        # print(d)
        max_ = 1
        for key, value in d.items():
            # if key >= value:
            max_ = max(max_, min(key, value))
        return max_