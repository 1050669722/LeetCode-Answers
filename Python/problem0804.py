# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 09:42:46 2019

@author: ASUS
"""

class Solution:
    def uniqueMorseRepresentations(self, words: list) -> int:
        self.M = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for k in range(len(words)):
            words[k] = self.convert(words[k])
        return len(set(words))
        
    def convert(self, word):
#        word = list(word)
#        length = len(word)
#        for letter in word:
#            word.append(self.M[ord(letter) - ord('a')])
#        word.reverse()
#        for _ in range(length):
#            word.pop()
#        word.reverse()
#        return ''.join(word)
        word = list(word)
        for k in range(len(word)):
            word[k] = self.M[ord(word[k]) - ord('a')]
        return ''.join(word)
        
        
        
        
solu = Solution()
words = ["gin", "zen", "gig", "msg"]
print(solu.uniqueMorseRepresentations(words))