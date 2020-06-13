# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:43:48 2019

@author: ASUS
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        X, Y = [], []
        while x:
            tmp = x%2
            X.append(tmp)
            x //= 2
        while y:
            tmp = y%2
            Y.append(tmp)
            y //= 2
        lendiff = len(X) - len(Y)
        if lendiff > 0:
            for _ in range(lendiff):
                Y.append(0)
        elif lendiff < 0:
            for _ in range(abs(lendiff)):
                X.append(0)
        X.reverse()
        Y.reverse()
        count = 0
        for k in range(len(X)):
            if X[k] != Y[k]:
                count += 1
        return count
    
solu = Solution()
x, y = 1, 4
print(solu.hammingDistance(x, y))