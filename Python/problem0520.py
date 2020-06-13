# -*- coding: utf-8 -*-
"""
Created on Wed May 29 10:06:53 2019

@author: Administrator
"""

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        count = 0
        for k in word:
            if 'A'<=k and k<='Z':
                count += 1
        if count == len(word):
            return True
        count = 0
        for k in word:
            if 'a'<=k and k<='z':
                count += 1
        if count == len(word):
            return True
        count = 0
        if 'A'<=word[0] and word[0]<='Z':
            for k in range(1, len(word)):
                if 'a'<=word[k] and word[k]<='z':
                    count += 1
            if count + 1 == len(word):
                return True
        return False
        
        
solu = Solution()
word = 'USA'
#word = 'FlaG'
#word = 'leetcode'
#word = 'Google'
print(solu.detectCapitalUse(word))