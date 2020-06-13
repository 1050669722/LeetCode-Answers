# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 13:34:55 2019

@author: ASUS
"""

class Solution:
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
#        length = len(arr)
#        for k in range(len(arr)):
#            if arr[k] == 0:
#                arr.append(0)
#        for k in range(length):
#            if arr[k] == 0:
#                tmp = arr[(k+1):(k+1+length-1)]
#                tmp.pop()
#                tmp = [0] + tmp
#                arr[(k+1):(k+1+length-1)] = tmp
        
        k = 0
        count = 0
        while k < len(arr):
            if arr[k] == 0:
                arr.insert(k, 0)
                k += 1
                count += 1
            k += 1
        for p in range(count):
            arr.pop()
        
solu = Solution()
arr = [1,0,2,3,0,4,5,0]
#arr = [1,2,3]
solu.duplicateZeros(arr)
print(arr)