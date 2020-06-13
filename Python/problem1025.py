# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:36:28 2019

@author: Administrator
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
#        for k in range(N-1, 0, -1):
#            if N%k == 0:
#                self.divisorGame(N-k)
#        return N-1-k % 2 == 0

        if N<=1:
            return False
        else:
            target = [0 for _ in range(N+1)]
            target[1] = 1
            target[2] = 1
            for i in range(3, N+1):
                for j in range(1, i):#for j in range(1, i//2):#
                    if i%j == 0 and target[i-j] == 0:
                        target[i] == 1
                        break
            return target[N] == 1
    
solu = Solution()
N = 2
#N = 3
N = 4
print(solu.divisorGame(N))