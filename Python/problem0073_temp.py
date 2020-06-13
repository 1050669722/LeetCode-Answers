# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:02:15 2019

@author: Administrator
"""

class Solution:
    def setZeroes(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        d = {}
        d['R'] = []
        d['C'] = []
        for r, val in enumerate(matrix):
            for c, v in enumerate(val):
                if v == 0:
                    d['R'].append(r)
                    d['C'].append(c)
        d['R'] = list(set(d['R']))
        d['C'] = list(set(d['C']))
        for p in range(len(matrix)):
            for q in range(len(matrix[p])):
                if p in d['R'] or q in d['C']:
                    matrix[p][q] = 0
        
solu = Solution()
matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
solu.setZeroes(matrix)
print(matrix)