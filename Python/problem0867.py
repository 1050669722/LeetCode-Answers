# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:38:21 2019

@author: Administrator
"""

class Solution:
    def transpose(self, A: list) -> list:
        if not A:
            return A
        m = len(A)
        n = len(A[0])
        B = []
        for k in range(n):
            B.append([0]*m)
#        B = [0] * m
#        B = [([0] * m).copy()] * n
#        B = [[0,0],[0,0],[0,0]]
        for p in range(len(B)):
            for q in range(len(B[0])):
                B[p][q] = A[q][p]
#                print(p,q)
#                print(A[q][p])
#                print(B)
        return B
        
solu = Solution()
A = [[1,2,3],[4,5,6],[7,8,9]]
#A = [[1,2,3],[4,5,6]]
A = []
print(solu.transpose(A))