# -*- coding: utf-8 -*-
"""
Created on Sat May 25 17:27:57 2019

@author: Administrator
"""

import time

time1 = time.perf_counter()

class Solution:
    def fib(self, N: int) -> int:
#        if N == 0:
#            return 0
#        if N == 1:
#            return 1
#        return self.fib(N-1) + self.fib(N-2)
#        if N == 0:
#            return 0
#        if N == 1:
#            return 1
#        a = [0, 1]
#        for k in range(2, N+1):
#            a.append( a[k-1]+a[k-2] )
#        return a[-1]
        
#        import numpy as np
#        if N == 0:
#            return 0
#        if N == 1:
#            return 1
##        a = [0, 1]
#        Q = np.array( [[1, 1], [1, 0]] ).astype('float64')
#        P = Q.copy()
##        for k in range():
##        return (Q**(N-2))[0][0]
#        for k in range(2, N):
#            Q = np.dot(Q, P)
#        return Q[0][0]
        
        if N == 0:
            return 0
        if N == 1:
            return 1
        import numpy as np
        Q = np.array( [[1, 1], [1, 0]] ).astype('float64')
#        P = Q.copy()
#        for k in range(2, N):
#            Q = np.dot(Q, P)
#        a = []
#        a.append(Q, )
        Q = self.power(Q, N-1)
        return Q[0][0]
        
    def power(self, a, b):
        if b == 0:
            return 1
        if b == 1:
            return a
        import numpy as np
        temp = self.power(a, b//2)
        if b % 2 == 0:
            return np.dot(temp, temp)
        if b % 2 != 0:
            return np.dot(np.dot(temp, temp), a)

solu = Solution()
N = 3
#N = 2
N = 30
N = 100
print(solu.fib(N))


time2 = time.perf_counter()
print(time2-time1)


