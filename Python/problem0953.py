from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for k, letter in enumerate(order):
            d[letter] = chr(ord('a') + k)
        # print(d)

        for p in range(len(words)):
            words[p] = list(words[p])
            for q in range(len(words[p])):
                words[p][q] = d[words[p][q]]
            words[p] = ''.join(words[p])

        return words == sorted(words)

words = ["hello","leetcode"]; order = "hlabcdefgijkmnopqrstuvwxyz"
words = ["word","world","row"]; order = "worldabcefghijkmnpqstuvxyz"
words = ["apple","app"]; order = "abcdefghijklmnopqrstuvwxyz"
solu = Solution()
print(solu.isAlienSorted(words, order))