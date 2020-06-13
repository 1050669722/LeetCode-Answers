# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:36:10 2019

@author: ASUS
"""

class Solution:
    def anagramMappings(self, A: list, B: list) -> list:
        from collections import defaultdict
        d = defaultdict(int)
        for k in range(len(B)):
            d[B[k]] = k
        for k in range(len(A)):
            A[k] = d[A[k]]
        return A
        
solu = Solution()
A, B = [12, 28, 46, 32, 50], [50, 12, 32, 46, 28]
print(solu.anagramMappings(A, B))