# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 09:41:17 2019

@author: ASUS
"""

class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        base = [[1],[1,1]]
        if numRows == 2:
            return base
        for k in range(2, numRows):
            List = [0] * (k+1)
            List[0] = 1
            List[k] = 1
            for p in range(1, k): # index: [1, k-1]
                List[p] = base[k-1][p] + base[k-1][p-1]
            base.append(List)
        return base
        
        
solu = Solution()
numRows = 5
print(solu.generate(numRows))