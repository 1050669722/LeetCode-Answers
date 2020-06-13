from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            mark = 1
            d = self.reset(chars)
            for w in word:
                try:
                    d[w] -= 1
                except:
                    mark = 0
                    break
            if mark and self.isAvailable(d):
                # print(word)
                ans += len(word)
        return ans

    def reset(self, chars):
        d = {}
        for char in chars:
            try:
                d[char] += 1
            except:
                d[char] = 1
        return d

    def isAvailable(self, d):
        for value in d.values():
            if value < 0:
                return False
        return True

solu = Solution()
words, chars = ["cat","bt","hat","tree"], "atach"
print(solu.countCharacters(words, chars))