# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 08:57:45 2019

@author: ASUS
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        p, q = 0, len(S)-1
        S = list(S)
        while p < q:
            if ord('a')<=ord(S[p].lower())<=ord('z') and ord('a')<=ord(S[q].lower())<=ord('z'):
                S[p], S[q] = S[q], S[p]
                p += 1
                q -= 1
            else:
                if not ord('a')<=ord(S[p].lower())<=ord('z'):
                    p += 1
                if not ord('a')<=ord(S[q].lower())<=ord('z'):
                    q -= 1
        return ''.join(S)
        
solu = Solution()
S = "ab-cd"
#S = "a-bC-dEf-ghIj"
#S = "Test1ng-Leet=code-Q!"
print(solu.reverseOnlyLetters(S))