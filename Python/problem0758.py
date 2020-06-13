class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        wordDicts = []
        for word in words:
            d = {}
            for k in range( len(word)-1 ):
                d[word[k]] = d[word[k+1]]
            d[word[-1]] = ''
            wordDicts.append(d)

        positions_start, positions_end = [], []
        for k in range(len(S)):
            for wordDict in wordDicts:
                try:
                    wordDict[S[k]]
                except:
                    continue

solu = Solution()
words, S = ["ab", "bc"], "aabcd"
print(solu.boldWords(words, S))