# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:51:05 2019

@author: Administrator
"""

class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
#        a = [x for x in matrix]
        a = []
        for k in matrix:
            a += k
        head = 0
        tail = len(a) - 1
        while head <= tail:
            mid = (head + tail) // 2
            if a[mid] > target:
                tail = mid - 1
            elif a[mid] < target:
                head = mid + 1
            else:
#                print(head, mid, tail)
#                print(a[head], a[mid], a[tail])
                return True
        return False
        
        
        
        
solu = Solution()
matrix, target = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3
#matrix, target = [
#  [1,   3,  5,  7],
#  [10, 11, 16, 20],
#  [23, 30, 34, 50]
#], 13
matrix, target = [[1]], 0
print(solu.searchMatrix(matrix, target))