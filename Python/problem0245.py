# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 11:26:36 2019

@author: Administrator
"""

class Solution:
    def shortestWordDistance(self, words: list, word1: str, word2: str) -> int:
#        if word1 != word2:
#            p, q = -1, -1
#            ans = len(words) - 1
#            for idx, word in enumerate(words):
#                if word == word1: p = idx
#                if word == word2: q = idx
#                if (p!=-1) and (q!=-1): ans = min(ans, abs(p-q))
#            return ans
#        else:
         p = -1
         ans = len(words) - 1
         for idx, word in enumerate(words):
            if word == word1 or word == word2:
                if p != -1:
                    ans = min(ans, abs(p-idx))
                p = idx
         return ans
        
        
solu = Solution()
words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "coding", "practice"
#words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "makes", "coding"
#words, word1, word2 = ["a","c","b","a"], 'a', 'b'
words, word1, word2 = ["practice", "makes", "perfect", "coding", "makes"], "makes", "makes"
print(solu.shortestWordDistance(words, word1, word2))