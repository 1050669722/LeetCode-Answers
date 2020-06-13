from typing import List
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = list(paragraph)
        # print(paragraph)
        for k in range(len(paragraph)):
            if not (65<=ord(paragraph[k])<=90 or 97<=ord(paragraph[k])<=122):
                paragraph[k] = '.'
        paragraph = ''.join(paragraph)
        p = paragraph.split('.')
        p = [x.lower() for x in p]
        b = [x.lower() for x in banned]
        b = set(b)
        d = Counter(p)
        # print(p)
        # print(b)
        # print(d)
        # print(ord('A')) #65
        # print(ord('Z')) #90
        # print(ord('a')) #97
        # print(ord('z')) #122
        max_ = 0
        for k, v in d.items():
            if k and k not in b and v > max_:
                ans = k
                max_ = v
        return ans

paragraph, banned = "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
paragraph, banned = "Bob. hIt, baLl", ["bob", "hit"]
solu = Solution() #!?',;.
print(solu.mostCommonWord(paragraph, banned))