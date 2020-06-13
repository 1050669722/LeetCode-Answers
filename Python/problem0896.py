# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 11:12:28 2019

@author: Administrator
"""

class Solution:
    def isMonotonic(self, A: list) -> bool:
        if len(A)<=1:
            return True
        if A[1] > A[0]:
            return self.fun1(A)
        elif A[1] < A[0]:
            return self.fun2(A)
        else:
            for k in range(2, len(A)):
                if A[k] > A[k-1]:
                    return self.fun1(A[k:])
                elif A[k] < A[k-1]:
                    return self.fun2(A[k:])
            return True
                
    def fun1(self, A):
        for k in range(2, len(A)):
            if A[k] < A[k-1]:
                return False
        return True
        
    def fun2(self, A):
        for k in range(2, len(A)):
            if A[k] > A[k-1]:
                return False
        return True
        
        
solu = Solution()
A = [1,2,2,3]
#A = [6,5,4,4]
#A = [1,3,2]
#A = [1,2,4,5]
#A = [1,1,1]
A = [1,1,0]
print(solu.isMonotonic(A))