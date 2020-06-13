# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:00:39 2019

@author: Administrator
"""

class Solution:
    def flipAndInvertImage(self, A: list) -> list:
        for a in A:
            p, q = 0, len(a)-1
            while p<=q:
                if p == q:
                    a[p] = 1 - a[p]
                    break
                a[p], a[q] = a[q], a[p]
                a[p] = 1 - a[p]
                a[q] = 1 - a[q]
                p += 1
                q -= 1
        return A
        
solu = Solution()
#A = [[1,1,0],[1,0,1],[0,0,0]]
A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
print(solu.flipAndInvertImage(A))