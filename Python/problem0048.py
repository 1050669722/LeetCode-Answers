# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:03:36 2019

@author: Administrator
"""

class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for p in range(len(matrix)):
            for q in range(p, len(matrix[0])):
                matrix[p][q], matrix[q][p] = matrix[q][p], matrix[p][q]
        for p in range(len(matrix)):
            matrix[p].reverse()
        
        
solu = Solution()
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
matrix = [[ 5, 1, 9,11],
          [ 2, 4, 8,10],
          [13, 3, 6, 7],
          [15,14,12,16]]
solu.rotate(matrix)
print(matrix)