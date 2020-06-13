# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:43:22 2019

@author: Administrator
"""

class Solution:
    def shortestDistance(self, words: list, word1: str, word2: str) -> int:
#        d = {}
#        d[word1], d[word2] = [], []
#        sd = len(words) - 1
#        for k in range(len(words)):
#            if words[k] == word1 or words[k] == word2:
#                d[words[k]].append(k)
#                if d[word1] and d[word2]:
#                    sd = min(sd, abs(d[word1][-1] - d[word2][-1]))
##                    if sd > abs(d[word1][-1] - d[word2][-1]):
##                        sd = abs(d[word1][-1] - d[word2][-1])
#        return sd
        
#        p, q = -1, -1
#        ans = len(words) - 1
#        for idx, word in enumerate(words):
#            if word == word1: p = idx
#            if word == word2: q = idx
#            if (p!=-1) and (q!=-1): ans = min(ans, abs(p-q))
#        return ans
        
#        p, q = -1, -1
#        ans = len(words) - 1
#        for idx, word in enumerate(words):
#            if word == word1 or word == word2:
#                if word == word1:
#                    p = idx
#                else:
#                    q = idx
#                if (p!=-1) and (q!=-1):
#                    ans = min(ans, abs(p-q))
#        return ans
        
        from collections import defaultdict
        d = defaultdict(list)
        for idx, word in enumerate(words):
            d[word].append(idx)
#        d = {}
#        for idx, word in enumerate(words):
#            try:
#                d[word].append(idx)
#            except:
#                d[word] = []
#                d[word].append(idx)
        ans = len(words) - 1#100000#
        print(ans)
        p, q = 0, 0
        while p<len(d[word1]) and q<len(d[word2]):
            ans = min(ans, abs(d[word1][p] - d[word2][q]))
            if d[word1][p] < d[word2][q]:
                p += 1
            else:
                q += 1
#        print(d)
        return ans
            
        
solu = Solution()
words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
#words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"
#words, word1, word2 = ["a","c","b","a"], 'a', 'b'
words, word1, word2 = ["a","b","c","d","d"], 'a', 'd'
words, word1, word2 = ["this","is","a","long","run","sentence","is","fun","day","today","sunny","weather","is","a","day","tuesday","this","sentence","running","rainy"], "running", "run"
print(solu.shortestDistance(words, word1, word2))