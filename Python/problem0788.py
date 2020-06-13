# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 10:59:35 2019

@author: Administrator
"""

class Solution:
    def rotatedDigits(self, N: int) -> int:
        count = 0
        for n in range(1, N+1):
            mark = 0
            m = n
            while n:
                tmp = n % 10
                n = n // 10
                if tmp in [3, 4, 7]:
                    mark = len(str(m))
                    break
                elif tmp in [0, 1, 8]:
                    mark += 1
#            print(mark)
            if mark != len(str(m)):
                count += 1
#                print(m)
        return count
        
solu = Solution()
N = 10
#N = 10000
#N = 857
#N = 818
print(solu.rotatedDigits(N))