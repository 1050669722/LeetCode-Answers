# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:47:24 2019

@author: Administrator
"""

class WordDistance:

    def __init__(self, words: list):
#        self.list = list
        
        from collections import defaultdict
        self.d = defaultdict(list)
        for idx, word in enumerate(words):
            self.d[word].append(idx)
#        self.d = {}
#        for idx, word in enumerate(words):
#            try:
#                self.d[word].append(idx)
#            except:
#                self.d[word] = []
#                self.d[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
#        p, q = -1, -1
#        ans = len(self.list) - 1
#        for idx, word in enumerate(self.list):
#            if word == word1 or word == word2:
#                if word == word1:
#                    p = idx
#                else:
#                    q = idx
#                if (p!=-1) and (p!=-1):
#                    ans = min(ans, abs(p-q))
#        return ans
        
        lengthSum = 0
        for k, v in self.d.items():
            lengthSum += len(v)
        ans = lengthSum - 1 #有重复单词，所以words的长度不能写成len(self.d.keys())这样
        p, q = 0, 0
        while p<len(self.d[word1]) and q<len(self.d[word2]):
            ans = min(ans, abs(self.d[word1][p] - self.d[word2][q]))
            if self.d[word1][p] < self.d[word2][q]:
                p += 1
            else:
                q += 1
        return ans


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)