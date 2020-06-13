class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        d = {}
        for k in range(len(keyboard)):
            d[keyboard[k]] = k
        ans = d[word[0]] - 0
        for k in range(1, len(word)):
            ans += abs(d[word[k]] - d[word[k-1]])
        return ans


